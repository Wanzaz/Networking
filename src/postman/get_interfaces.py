import requests
import sy

# Allow self signed certs
requests.packages.urllib3.disable_warnings()
# Credentials
USER = 'developer'
PASS = 'C1sco12345'


# URL for GET request
url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"
# Set yang+json as the data formats
headers = {'Content-Type': 'application/yang-data+json',
'Accept': 'application/yang-data+json'}
# Run GET
response = requests.get(url, auth=(USER, PASS),
headers=headers, verify=False)

print(response.text)
