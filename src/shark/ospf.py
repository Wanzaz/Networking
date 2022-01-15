
import pyshark

capture = pyshark.LiveCapture('eth0')
myfile = open('ospfpassword.txt', 'w')


for packet in capture:
    if 'OSPF' in packet:
        ospfpassword = 'OSPF password: ' + packet.ospf.auth_simple
        myfile.write(str(ospfpassword)'\n')

