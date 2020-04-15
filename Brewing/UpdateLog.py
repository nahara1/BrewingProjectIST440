# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 4/7/20
# Last Date Changed: 4/13/2020
# Rev 3

import requests
import TeamBoiling.Boil
# import each team's file where logging will be ran


# status_log will come from each team
# e.g. status_log = "{\"prep_stage\":\"Started Prep\"}"
# status_log = "{\"mashing_stage\":\"Started Mashing\"}"
# status_log = "{\"boiling_stage\":\"Started Boiling\"}"
# status_log = "{\"ferment_stage\":\"Started Fermenting\"}"
# status_log = "{\"kegging_stage\":\"Started Kegging\"}"

log = TeamBoiling.Boil.Boil.status_log
# prep_log
# mashing_log
# ferment_log
# kegging_log

# row_id is the sys_id that will come from when CreateLog.py runs
# row_id = sysID
row_id = '339f13db1b40d010076b777c0a4bcb0f'


class UpdateLog():

    url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_logging/' + row_id

    # User name="IST440", Password="IST440" for everyong
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
