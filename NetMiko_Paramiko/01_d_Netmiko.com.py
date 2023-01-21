from netmiko import Netmiko


my_switch = Netmiko(ip='192.168.122.12',
                    username='puma',
                    password= 'cisco',
                    device_type='cisco_ios')


print("-----Connected to the device----")
command1 = my_switch.send_command('show run')
print(command1)

with open('netmiko_backup.txt1', 'w') as my_data:
    my_data.write(command1)

