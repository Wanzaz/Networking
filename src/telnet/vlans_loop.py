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

for n in range (2,11):
    tn.write(b"vlan " + str(n).encode("ascii") + b"\n)
    tn.write(b"name Python_VLAN_" + str(n).encode("ascii") + b"\n")

tn.write(b"end")
tn.write(b"exit")

print(tn.read_all().decode('ascii'))

