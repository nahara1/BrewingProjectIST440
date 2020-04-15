# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 4/7/20
# Last Date Changed: 4/13/2020
# Rev 3

#                            * * * Instructions * * *
# Team Prep runs CreateLog.py to create a new row in the Service Now "Logging" table
# After that, everyone runs UpdateLog.py to implement logging e.g. "Prep Stage has started",
# "Prep has finished", "Mashing has started", "Mashing finished successfully", etc.

import requests


class CreateLog():

    # URL for the Logging table
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_logging?'

    # User name="IST440", Password="IST440" for every user
    user = 'IST440'
    pwd = 'IST440'

    # Set proper headers
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    # Do the HTTP request - POST is the HTTP request to create a record
    # response = requests.post(url, auth=(user, pwd), headers=headers, data="{\"recipe_name\":\"Beer 3\"}")
    response = requests.post(url, auth=(user, pwd), headers=headers, data="{\"prep_stage\":\"Began Prep\"}")

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(data)
