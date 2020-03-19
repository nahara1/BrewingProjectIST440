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
url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_recipe?sysparm_limit=1'

# Username and Pass for Servicenow instance
user = 'dvz5048'
pwd = 'Raikira79'

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
print(data['result'])

for doc in datajson:
    try:
        for x in collection.find({},{'sys_id' : 1}):
            print(x)
            if doc['sys_id'] == x['sys_id']:
                print()
                print('sys_id duplicate - no document inserted')
            else:
                client.test.testrecipes.insert(doc)
                print('document inserted')
    except pymongo.errors.DuplicateKeyError:
        continue