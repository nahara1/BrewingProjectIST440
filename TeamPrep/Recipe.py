# Project: Brewing Automation System - Capstone Project
# Purpose Details:
# Course: IST 440W - 001
# Author: Antonio Rivera :)
# Date Developed: 4/9/20

class recipe:








class get_recipe:
    '''
    This class will pull data from ServiceNow to add to the attributes listed above
    '''
    # Need to install requests package for python
    # easy_install requests
    import requests

    # Set the request parameters
    url = ''

    # Eg. User name="admin", Password="admin" for this code sample.
    user = 'IST440'
    pwd = 'IST440'

    # Set proper headers
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    # Do the HTTP request
    response = requests.get(url, auth=(user, pwd), headers=headers)

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
    exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(data)