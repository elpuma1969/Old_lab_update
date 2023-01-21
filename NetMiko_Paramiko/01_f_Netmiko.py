import time

import paramiko

hostname = '192.168.122.12'
username = "puma"
password = 'cisco'

ssh_client = paramiko.client.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh_client.connect(hostname=hostname, port=22, username=username, password=password, look_for_keys=False,
                   allow_agent=False)
device_access = ssh_client.invoke_shell()
print("Connected")
device_access.send(b"term len 0\n")
device_access.send(b"show version\n")
time.sleep(3)

output = device_access.recv(65535).decode()
print(output)

