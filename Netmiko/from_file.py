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

    with ConnectHandler(**ios_device) as net_connect:
        output = net_connect.send_config_from_file("command_file")
    print(output)


