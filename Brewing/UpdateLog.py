# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 4/7/20
# Last Date Changed: 4/15/2020
# Rev 4

# To add logging to every team, where you want logging add the following lines:
# status_log = "{\"boiling_stage\":\"Started Boiling\"}"
# UpdateLog.UpdateLog.log_to_service_now(self, status_log)
# change "boiling" to your stage name in the Logging table
# e.g. prep_stage, mashing_stage, ferment_stage, kegging_stage

import requests

# Enter in sys_id after CreateLog.py runs
row_id = '998c0d841b141410076b777c0a4bcbb9'


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

        # Print Log statement
        print("Logged Message:", log)

