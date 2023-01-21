#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler

username = input('Enter your SSH username: ')
password = getpass()

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
        'username': username,
        'password': password,
        'port': 22,
    }

    connection = ConnectHandler(**ios_device)
    print('Entering the enable mode...')
    connection.enable()

    output = connection.send_config_set(commands_list)

    prompt = connection.find_prompt()
    hostname = prompt[0:-1]

    from datetime import datetime

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    filename = f'{hostname}_{year}-{month}-{day}_update.txt'

    with open(filename, 'w') as final:
        final.write(output)
        print(f'Backup of {hostname} completed successfully')
        print('#' * 30)

    print('Closing connection')
    connection.disconnect()
