# sudo apt install python3-pip
# sudo pip3 install -U netmiko

"""Python Script 3 Step 2
• Run Python remotely using Ubuntu VM: Print out interfaces to test our script:"""

#!/usr/bin/env python
from netmiko import ConnectHandler
nx_os = {
    'device_type': 'cisco_ios',
    'ip': 'sbx-nxos-mgmt.cisco.com',
    'username': 'admin',
    'password': 'Admin_1234!',
    'port': 8181
}

net_connect = ConnectHandler(**nx_os)
output = net_connect.send_command('show ip int brief')
print(output)
