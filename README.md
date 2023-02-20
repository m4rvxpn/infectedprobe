# InfectedProbe
InfectedProbe is capable of probing networks to identify vulnerabilities and weaknesses.



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
