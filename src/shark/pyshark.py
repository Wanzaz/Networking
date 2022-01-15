
import pyshark
capture = pyshark.LiveCapture(interface='eth0')
for packet in capture.sniff_continuosly(packet_count=50):
    myfile = open('pyshark.txt', 'w')
    myfile.write(str(packet))
    try:
        print('Source = ' + packet['ip'].src)
        print('Destination = ' + packet['ip'].dst)
        print('EIGRP AS= ' + packet['eigrp'].AS) 
    except:
        pass

print('The end')
exit()
