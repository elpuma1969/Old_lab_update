from netmiko import ConnectHandler

connection = ConnectHandler(host='192.168.122.12', port='22', username='puma', password='cisco',
                            device_type='cisco_ios')

output = connection.send_command('show ip interface brief')
print(output)

print('Closing Connection')
connection.disconnect()
