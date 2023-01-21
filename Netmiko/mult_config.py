#!/usr/bin/env python

from netmiko import ConnectHandler

with open('command_file') as f:
    commands_list = f.read().splitlines()

with open('devices_file') as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    print('Connecting to device" ' + devices)
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': 'puma',
        'password': 'cisco'
    }

    net_connect = ConnectHandler(**ios_device)
    output = net_connect.send_command("show vlan-sw")
    output2 = net_connect.send_config_set(commands_list)
    print(output + output2)



