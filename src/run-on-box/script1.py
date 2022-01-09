from cli import *

cmd1 = 'show ip int brief | json pretty'
output1 = cli(cmd1)
print(output1)

