# Project: IST 440 Barlog Brewery
# Purpose Details: To create a Recipe Class
# Course: IST 440
# Author: Asraa Alkurdi, Jinal Parmar, Anny Espinal
# Date Developed: 4/1/2020
# Last Date Changed: 4/1/2020
# Rev: 1

import json
import urllib.request

import requests

# Get the record from the table, save it as a json file and add it to a mongodb file
# Getting the record from the table
url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_recipe?sysparm_fields=sys_id%2Crecipe_name%2Ctype%2Cstyle%2Cog%2Cfg%2Cabv%2Cibu%2Cwater_volume%2Cwater_temperature%2Cgrain_bill%2Cboiling_duration%2Cyeast&sysparm_limit=100'
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
# Decoding the JSON response into a dictionary and use the data
data = response.json()
# print(data)
with open('data.json', 'w') as f:
    json.dump(data, f)

# Connecting to the DB
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['Retrieved Recipe']
collection_recipe = db['recipes']
with open('data.json') as f:
    file_data = json.load(f)
    collection_recipe.insert_one(file_data)
    client.close()
