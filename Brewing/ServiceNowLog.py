# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 4/7/20
# Last Date Changed: 4/16/2020
# Rev 4

import requests


class ServiceNowLog():

    def create_new_log(self, log):
        """
        Creates a log in the ServiceNow Logging table
        :param log: a status log message
        :return: void
        """
        # URL for the Logging table
        url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_log?'

        # User name="IST440", Password="IST440" for every user
        user = 'IST440'
        pwd = 'IST440'

        # Set proper headers
        headers = {"Content-Type": "application/json", "Accept": "application/json"}

        # Do the HTTP request - POST is the HTTP request to create a record
        response = requests.post(url, auth=(user, pwd), headers=headers, data=log)

        # Print Log
        print("Logged Message:", log)
