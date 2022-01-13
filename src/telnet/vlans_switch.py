#username david password cisco
#line vty 0 4
#login local
#transport input all
#telnet 192.168.122.71
#enable password cisco
#debug telnet

import getpass
import telnetlib

HOST = "192.168.122.71"
user = input("Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"ls\n")
tn.write(b"exit\n")
tn.write(b"conf t\n")
tn.write(b"vlan 2\n")
tn.write(b"name Python_VLAN_2\n")
tn.write(b"vlan 3\n")
tn.write(b"name Python_VLAN_3\n")
tn.write(b"vlan 4\n")
tn.write(b"name Python_VLAN_4\n")
tn.write(b"vlan 5\n")
tn.write(b"name Python_VLAN_5\n")
tn.write(b"end")
tn.write(b"exit")

print(tn.read_all().decode('ascii'))

