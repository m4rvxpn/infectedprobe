# InfectedProbe
InfectedProbe a powerful tool for security professionals to automate and streamline their penetration testing workflow. By using this package, you can save time and effort, and focus on the more important aspects of your work, such as analyzing and interpreting the results. InfectedProbe is capable of probing networks to identify vulnerabilities and weaknesses. 

It consists of a Python CLI that leverages masscan and nmap for network scanning, and Metasploit for exploit testing. The tool also includes a Flask-based RESTful API for managing workspaces and generating reports. The results are stored in an SQLite database for easy retrieval and analysis. InfectedProbe is designed for penetration testing and can help identify network vulnerabilities before an attacker exploits them.



## Getting started

### Usage Example

```$ python mycli.py
(Cmd) scan example.com
Starting masscan scan...
Masscan scan completed.
Starting nmap scan...
Nmap scan completed.
Inputted data to Metasploit database.
(Cmd) scan 192.168.1.1/24 10.0.0.1-10.0.0.10
Starting masscan scan...
Masscan scan completed.
Starting nmap scan...
Nmap scan completed.
Inputted data to Metasploit database.
(Cmd) scan example.com 192.168.1.1/24
Starting masscan scan...
Masscan scan completed.
Starting nmap scan...
Nmap scan completed.
Inputted data to Metasploit database.
(Cmd) scan invalidinput
Invalid input. Enter a domain, list of domains, IP/CIDR range, or list of IP/CIDR ranges.
(Cmd) exit
Exiting program...

```
