# Project: Brewing Automation System - Capstone Project
# Purpose Details: Employee Class
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/5
# Rev
class Employee:
    def __init__(self, employee_id, employee_name, employee_role):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_role = employee_role

    def get_employee_id(self):
        '''
        gets the employee id
        :return: employee id
        '''
        return self.employee_id

    def get_employee_name(self):
        '''
        gets the employee name
        :return: employee name
        '''
        return self.employee_name

    def get_employee_role(self):
        '''
        gets the employee role
        :return: employee role
        '''
        return self.employee_role


class get_employee:
    #Need to install requests package for python
    #easy_install requests
    import requests

    # Set the request parameters
    url = ''

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
