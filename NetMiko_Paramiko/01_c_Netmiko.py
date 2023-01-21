from netmiko import ConnectHandler

ESW1 = {
    "device_type": "cisco_ios",
    "host": "192.168.122.11",
    "username": "puma",
    "password": "cisco",
    "secret": "cisco" # Enable password
}

connection = ConnectHandler(**ESW1)
connection.enable() # Enable method

config_commands = ['interface fa1/4', 'des VLAN99_Check', 'EXIT', 'interface fa1/5', 'des PUMA_TEST', 'EXIT']
connection.send_config_set(config_commands)
print(config_commands)


print('Closing Connection')
connection.disconnect()

