#!/usr/bin/env python

from netmiko import ConnectHandler
import json

nx_os = {
'device_type': 'cisco_ios',
'ip': 'sbx-nxos-mgmt.cisco.com',
'username': 'admin',
'password': 'Admin_1234!',
'port': 8181
}

net_connect = ConnectHandler(**nx_os)
output = net_connect.send_command('show ip int brief | json-pretty')
json_data = json.loads(output)
int_number = len(json_data['TABLE_intf']['ROW_intf'])
for x in range(int_number):
    print(json_data['TABLE_intf']['ROW_intf'][x]['intf-name'])
    print(json_data['TABLE_intf']['ROW_intf'][x]['prefix'])
