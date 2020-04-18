#Need to install requests package for python
#easy_install requests
import requests


url = 'https://emplkasperpsu2.service-now.com/api/now/table/sys_user/fa4b8ecbdb170010fe33ffb41d961954?sysparm_fields=sys_updated_on%2Csys_updated_by%2Cuser_name%2Cfirst_name%2Clast_name%2Cstreet%2Ccity%2Cstate%2Czip%2Cemail'
'''
Sets the request parameters with ServiceNow url
'''

user = 'IST440'
pwd = 'IST440'
'''
Sets the Username and Password for ServiceNow
'''

headers = {"Content-Type":"application/json","Accept":"application/json"}
'''
Sets the proper headers
'''

response = requests.patch(url, auth=(user, pwd), headers=headers )
'''
Does HTTP request and authentication of headers
'''

if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()
    '''
    Checks for HTTP codes other than 200 
    '''

data = response.json()
print(data)
'''
Decodes the JSON response into a dictionary and uses the data
'''