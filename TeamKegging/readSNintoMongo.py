# GET
# install requests package, pymongo package
import requests
import pymongo
from pymongo import MongoClient
from dal import dal


dalHandler = dal('localhost', 27017)
# Connection to MongoDB
try:
    client = MongoClient(dalHandler.getHost(), dalHandler.getPort())
    # Select the Database
    db = client.test
    # Select the Collection
    collection = db.testrecipes
    # Select one Document
except:
    print("Cannot connect to the MongoDB")

# Set the request parameters
#url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_recipe?sysparm_limit=10'
url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_recipe?sysparm_fields=sys_id%2Crecipe_name%2Ctype%2Cstyle%2Cog%2Cfg%2Cabv%2Cibu%2Cwater_volume%2Cwater_temperature%2Cgrain_bill%2Cboiling_duration%2Cyeast&sysparm_limit=100'

# Username and Pass for Servicenow instance
user = 'IST440'
pwd = 'IST440'

# headers
headers = {"content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user,pwd), headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()

datajson = data['result']
#print(data['result'])

for doc in datajson:
    try:
        col_match = 0
        for x in client.test.testrecipes.find({},{'sys_id' : 1}):
            print('inserting document')

            if doc['sys_id'] == x['sys_id']:
                col_match += 1

        if col_match == 0:
            client.test.testrecipes.insert(doc)
            print('Document Inserted')
        if col_match > 0:
            print('sys_id duplicate - found ' + str(col_match) + ' duplicate(s) - no document inserted')

        #for x in client.test.testrecipes.find({}, {'_id': 0}):
            #print(x)
    except pymongo.errors.DuplicateKeyError:
        continue