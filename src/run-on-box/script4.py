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
output = net_connect.send_command('show ip int brief | json-pretty')
print(output)
