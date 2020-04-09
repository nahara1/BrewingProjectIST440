# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 4/7/20
# Last Date Changed: 4/7/2020
# Rev 1

import requests
import TeamBoiling.Boil


# status_log will come from each team
# status_log = "{\"ferment_stage\":\"Started Fermenting\"}"

log = TeamBoiling.Boil.Boil.status_log
row_id = '3fc73d3d1b0410107bd975541a4bcb5e'


class UpdateLog():

    url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_logging/' + row_id

    # User name="IST440", Password="IST440" for this code sample.
    user = 'IST440'
    pwd = 'IST440'

    # Set proper headers
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    # Do the HTTP request - PATCH is the HTTP request to update a record
    response = requests.patch(url, auth=(user, pwd), headers=headers, data=log)

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(data)
