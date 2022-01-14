#apt-get update
#apt-get instal tshark
#apt-get install python-pip
#pip3 install pyshark
#tshark
#tshark -w tshark1.pcap
Script:
import pyshark
cap = pyshark.FileCapture("tshark1.pcap")
print(cap[0])
cap[0].show()
print(cap[1].ip)
print(cap[1].eigrp)
print(cap[1].eigrp.AS) = autonomous system number
print(cap[1].eigrp.par_K1)
dir(cap[1])

#apt-get install wget
#wgtet https://github.com/gcla/termshark
#tar -xf termsshark_1.0.0_linux_x64.tar.gz
#termshark -r tshark1.pcap

