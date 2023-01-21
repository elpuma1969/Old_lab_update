#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

cisco1 = {
    "device_type": "cisco_ios",
    "host": "192.168.122.12",
    "username": "puma",
    "password": getpass(),
}

command = "copy running-config startup-config"
net_connect = ConnectHandler(**cisco1)
output = net_connect.send_command_timing(
        command_string=command, strip_prompt=False, strip_command=False
)
if "Delete filename" in output:
    output += net_connect.send_command_timing(
        command_string="\n", strip_prompt=False, strip_command=False
    )
if "?" in output:
    output += net_connect.send_command_timing(
        command_string="\n", strip_prompt=False, strip_command=False)

net_connect.disconnect()

print()
print(output)
print()
