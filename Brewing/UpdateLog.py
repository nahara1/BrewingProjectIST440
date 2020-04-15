# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 4/7/20
# Last Date Changed: 4/15/2020
# Rev 4

import requests

log = ''

# row_id is the sys_id that will come from when CreateLog.py runs
# row_id = sysID
row_id = '09b4f0481bd01410076b777c0a4bcb1a'


class UpdateLog():

    def log_to_service_now(self, log):
        url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_logging/' + row_id

        # User name="IST440", Password="IST440" for everyone
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

