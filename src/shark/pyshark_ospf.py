#monitor session 1 source interface Gi0/1
#monitor session 1 destination interface Gi0/0
#OSPF:

import pyshark

capture = pyshark.LiveCapture('eth0')
for packet in capture:
    if 'OSPF' in packet:
        print('OSPF password: ' + packet.ospf.auth_simple)
