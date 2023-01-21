#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

cisco1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.122.11",
    "username": "puma",
    "password": getpass()
}

# Show command that we execute
command = ["int FastEthernet1/6 ", "switchport access vlan 13", "spanning-tree portfast"]
command2 = ["int fa1/15", "no shutdown"]

with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_config_set(command + command2)
    output2 = net_connect.send_command("show ip int bri")
print(output + output2)
