#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

cisco1 = {
    "device_type": "cisco_ios",
    "host": "192.168.122.11",
    "username": "puma",
    "password": getpass()
}

intf = input("Enter Type of InterFace: ")
mode = input("Enter interface mode(access/trunk): ")
vlan = input("Enter number of vlan: ")

commands = [f"int fa{intf}\n",
            f"switchport mode {mode}\n",
            f"switchport access vlan {vlan}\n",
            f"switchport voice vlan 200"]


with ConnectHandler(**cisco1) as net_connect:
    output3 = net_connect.send_config_set(commands)
print(output3)
