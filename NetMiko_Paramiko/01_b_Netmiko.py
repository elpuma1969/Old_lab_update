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

which_prompt = connection.find_prompt() # Find prompt method
print(which_prompt) # Print the prompt

output = connection.send_command('show run')
print(output)

print('Closing Connection')
connection.disconnect()

