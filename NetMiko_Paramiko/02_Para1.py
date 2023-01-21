import time

import paramiko

ESW1 = {"hostname": '192.168.122.11',
        "username": 'puma',
        "password": "cisco"}


def cisco_backup(hostname, username, password):
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname=hostname, port=22, username=username, password=password, look_for_keys=False,
                       allow_agent=False)
    device_access = client.invoke_shell()
    print("Connected")
    device_access.send(b"term len 0\n")
    device_access.send(b"show version\n")
    time.sleep(3)

    output = device_access.recv(65535).decode()
    print(output)

    with open("paramiko_backup.txt", "w") as p_data:
        p_data.write(output)
    client.close()


cisco_backup(**ESW1)
