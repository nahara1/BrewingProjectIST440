# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 4/7/20
# Last Date Changed: 4/7/2020
# Rev 1

import requests

test = "{\"Boiling Stage \":\"Started Boiling\"}"


class CreateLog():

    # Set the request parameters

    url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_logging?'

    """
    To specify a number of records to be returned, add sysparm_limit=

    Eg. if you want to return 100 records, set url to: 

    url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_recipe?sysparm_limit=100'

    """

    # User name="IST440", Password="IST440" for this code sample.
    user = 'IST440'
    pwd = 'IST440'

    # Set proper headers
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    # Do the HTTP request - POST is the HTTP request to create a record
    # response = requests.post(url, auth=(user, pwd), headers=headers, data="{\"recipe_name\":\"Beer 3\"}")
    response = requests.post(url, auth=(user, pwd), headers=headers, data="{\"Boiling Stage \":\"Started Boiling\"}")

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(data)
