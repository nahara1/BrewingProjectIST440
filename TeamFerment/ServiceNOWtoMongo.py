# Project: IST 440 Barlog Brewery
# Purpose Details: Communication between ServiceNOW and MongoDB to display Lager recipe information
# Course: IST 440
# Author: Asraa Alkurdi, Jinal Parmar, Anny Espinal
# Date Developed: 4/1/2020
# Last Date Changed: 4/1/2020
# Rev: 1

import json
import urllib.request

import requests
from pymongo import MongoClient

"""
This class was created to pull information from ServiceNOW to MongoDB for the Brew Master to view whilst making a batch 
of Lager.
"""

class ServiceNOWtoMongo:

    """

    """
    def get_recipe(self):
        """
        This Try block ensures the URL of the ServiceNOW database, as well as the user log in credentials.
        """
        try:

            """
              The contents printed are needed to connect to the Local Host, and to provide logging messages, confirming 
              the recipe has been retrieved. 
            """
            url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_recipe?sysparm_fields=sys_id%2Crecipe_name%2Ctype%2Cstyle%2Cog%2Cfg%2Cabv%2Cibu%2Cwater_volume%2Cwater_temperature%2Cgrain_bill%2Cboiling_duration%2Cyeast&sysparm_limit=100'
            user = 'IST440'
            pwd = 'IST440'

            # Set proper headers
            headers = {"Content-Type": "application/json", "Accept": "application/json"}

            # Do the HTTP request
            response = requests.get(url, auth=(user, pwd), headers=headers)
            data = response.json()

            # print(data)
            """
              The contents printed are needed to connect to the Local Host, and to provide logging messages, confirming 
              the recipe has been retrieved. 
            """


            with open('data.json', 'w') as f:
                json.dump(data, f)


            client = MongoClient('localhost', 27017)
            db = client['Retrieved Recipe']
            collection_recipe = db['recipes']

            with open('data.json') as f:
                """
                This loads the retrieved information into a JSON File. 
                """
                file_data = json.load(f)
                collection_recipe.insert_one(file_data)

                client.close()


        except Exception:
            """
            This exception ensures the HTTP is 200.
            """
            # Check for HTTP codes other than 200
            if response.status_code != 200:
                print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
                exit()
