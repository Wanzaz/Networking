#Python and Linux on Cisco IOS?
#sh version
#iox
#sh iox-service
#interface virtualportGroup 0 
#ip unnumbered GigabitEthernet 1
#guestshell enable virtualPortGroup 0 guest-ip 10.1.1.2

#guestshell run bash
#vi

import sys
import cli
cli.executep(‘show ip int brief’)
cli.executep(‘show ver | include Version’)

#guestshell run python guestshell.py

