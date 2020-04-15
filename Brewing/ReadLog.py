# Project: Brewing Automation System - Capstone Project
# Purpose Details: To provide a sample code of how to read records from a ServiceNow table
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 4/14/2020
# Last Date Changed: 4/14/2020
# Rev 1

import requests


class ReadLog():

    # Set the request parameters
    # URL for the Logging table
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_logging?'

    # User name="IST440", Password="IST440" for this code sample.
    user = 'IST440'
    pwd = 'IST440'

    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

    # Do the HTTP request - GET is the HTTP request to read records
    response = requests.get(url, auth=(user, pwd), headers=headers)

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(data)

    # Get sys_id for row_id
    sysID = data['result'][0]['sys_id']
    print("sys_id: " + sysID)
