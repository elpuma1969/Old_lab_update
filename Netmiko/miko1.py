#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

cisco1 = {
    "device_type": "cisco_ios",
    "host": "192.168.122.11",
    "username": "puma",
    "password": getpass(),
}

# Show command that we execute
command = "show int status"
with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)

# Automatically cleans-up the output so that only the show output is returned
print()
print(output)
print()

