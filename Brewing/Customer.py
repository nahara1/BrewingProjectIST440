# Project: Brewing Automation System - Capstone Project
# Purpose Details: Class for the Customer data
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: Development Phase
# Last Date Changed: 4/8/2020
class Customer:
    def __init__(self, customer_id, customer_name, customer_address, customer_phone, customer_email):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_address = customer_phone
        self.customer_address = customer_email
        customer_id = int
        customer_name = str
        customer_address = str
        customer_phone = int
        customer_email = str

    def get_customer_id(self):
        '''
        gets the customer id
        :return: customer id
        '''
        return self.customer_id

    def get_customer_name(self):
        '''
        gets the customer name
        :return: customer name
        '''
        return self.customer_name

    def get_customer_address(self):
        '''
        gets the customer address
        :return: customer address
        '''
        return self.customer_address

    def get_customer_phone(self):
        '''
        gets the customer phone number
        :return: customer phone number
        '''
        return self.customer_phone

    def get_customer_email(self):

        '''
        gets the customer email
        :return: customer email
        '''
        return self.customer_email
#Need to install requests package for python
#easy_install requests
import requests

# Set the request parameters
url = 'https://emplkasperpsu2.service-now.com/api/now/table/sys_user?sysparm_fields=first_name%2Clast_name%2Cemail%2Chome_phone%2Cstreet%2Ccity%2Cstate%2Czip&sysparm_limit=20'

# Eg. User name="admin", Password="admin" for this code sample.
user = 'IST440'
pwd = 'IST440'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
