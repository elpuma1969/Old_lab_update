from netmiko import Netmiko
import difflib
import webbrowser

my_switch = Netmiko(ip='192.168.122.11',
                    username='puma',
                    password='cisco',
                    device_type='cisco_ios')


print("-----Connected to the device----")
command1 = my_switch.send_command('show run')
print(command1)

with open('netmiko_new_backup.txt', 'w') as my_data:
    my_data.write(command1)

ref = open("netmiko_backup.txt")
ref_content = ref.readlines()
print(ref_content)
ref.close()

new = open('netmiko_new_backup.txt')
new_content = new.readlines()
new.close()

conf_compare = difflib.HtmlDiff().make_file(fromlines=ref_content, tolines=new_content, fromdesc="Reference Config",
                                            todesc="Current config")

print(conf_compare)

with open("diff.html", "w") as new_diff:
    new_diff.write(conf_compare)

webbrowser.open_new_tab('diff.html')

print("-----Backup completed----")

my_switch.disconnect()

