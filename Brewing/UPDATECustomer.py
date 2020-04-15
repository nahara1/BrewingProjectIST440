# Project: Brewing Automation System - Capstone Project
# Purpose Details: Updated Customer data
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: Development Phase
# Last Date Changed: 4/8/2020

#Need to install requests package for python
#easy_install requests
import requests

# Set the request parameters
url = 'https://emplkasperpsu2.service-now.com/api/now/table/sys_user/fa4b8ecbdb170010fe33ffb41d961954?sysparm_fields=sys_updated_on%2Csys_updated_by%2Cuser_name%2Cfirst_name%2Clast_name%2Cstreet%2Ccity%2Cstate%2Czip%2Cemail'

# Eg. User name="admin", Password="admin" for this code sample.
user = 'IST440'
pwd = 'IST440'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.patch(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)