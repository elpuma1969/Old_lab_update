from netmiko import BaseConnection


# Create a subclass of BaseConnection for a specific device type (e.g. Cisco IOS)
class CiscoIOSConnection(BaseConnection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def disable_paging(self, *args, **kwargs):
        # Implement device-specific paging disable command
        self.send_command("terminal length 0")

    def connect(self):
        pass


# Create an instance of the CiscoIOSConnection class


ios_device = {
    "device_type": "cisco_ios",
    "ip": "192.168.122.11",
    "username": "puma",
    "password": "cisco",
    "port": 22,
}
conn = CiscoIOSConnection(**ios_device)

# Connect to the device
conn.connect()

# Disable paging on the device (using the device-specific method implemented in the subclass)
conn.disable_paging()

# Send a command to the device and print the output
output = conn.send_command("show run")
print(output)

# Close the connection
conn.disconnect()
