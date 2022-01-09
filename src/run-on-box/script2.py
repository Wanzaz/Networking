from cli import *
import json

cmd1 = 'show ip int brief | json pretty'
json_data = cli(cmd1)
json_final = json.loads(json_data)
print(json_final["TABLE_intf"] ["ROW_intf"] [0] ["prefix"])

