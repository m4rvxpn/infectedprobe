import cmd2
import subprocess
import re
from pymetasploit3.msfrpc import MsfRpcClient
from pymetasploit3.msfconsole import MsfRpcConsole
import json

class MyCLI(cmd2.Cmd):

    def __init__(self):
        super().__init__()
        self.prompt = 'cli> '
        self.msfrpc_client = None
        
    @cmd2.with_argument_list
    def do_scan(self, arglist):
        """Scan domains or IP addresses"""
        input_data = []
        for arg in arglist:
            if self.is_domain(arg):
                input_data.append(arg)
            elif self.is_cidr(arg):
                input_data.append(arg)
            elif self.is_ip_address(arg):
                input_data.append(arg)
            else:
                self.perror(f"Invalid input: {arg}")
                return
        
        # Run masscan against identified ports
        masscan_output = self.run_masscan(input_data)
        open_ports = self.get_open_ports(masscan_output)

        # Run nmap scan against open ports
        nmap_output = self.run_nmap(input_data, open_ports)

        # Input results to Metasploit database
        self.input_to_metasploit(nmap_output)
        
    def is_domain(self, arg):
        """Check if argument is a domain"""
        return re.match(r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+$", arg) is not None
    
    def is_cidr(self, arg):
        """Check if argument is a CIDR notation"""
        return re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}$", arg) is not None
    
    def is_ip_address(self, arg):
        """Check if argument is an IP address"""
        return re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", arg) is not None
    
    def run_masscan(self, input_data):
        """Run masscan scan"""
        input_args = ['masscan', '-p1-65535']
        input_args += input_data
        return subprocess.run(input_args, capture_output=True, text=True).stdout
    
    def get_open_ports(self, masscan_output):
        """Get open ports from masscan output"""
        open_ports = []
        for line in masscan_output.split('\n'):
            if 'open' in line:
                port = line.split()[2]
                open_ports.append(port)
        return open_ports
    
    def run_nmap(self, input_data, open_ports):
        """Run nmap scan against open ports"""
        input_args = ['nmap', '-p', ','.join(open_ports)]
        input_args += input_data
        return subprocess.run(input_args, capture_output=True, text=True).stdout
    
    def input_to_metasploit(self, nmap_output):
        """Input nmap output to Metasploit database"""
        if not self.msfrpc_client:
            self.msfrpc_client = MsfRpcClient('password')
            self.msfrpc_console = MsfRpcConsole(self.msfrpc)
            # Import nmap output to Metasploit database
            json_report = json.dumps({'ports':nmap_output})
            self.msfrpc_client.call('db.import_data', 'nmap', json_report)
            self.poutput('Inputted data to Metasploit database.')

    def onecmd(self, line):
        """Override default onecmd to handle KeyboardInterrupt"""
        try:
            return super().onecmd(line)
        except KeyboardInterrupt:
            self.poutput('\nExiting program...')
            return True
        
    def do_exit(self, arg):
        """Exit the program"""
        self.poutput('Exiting program...')
        return True

