# GET
# install requests package, pymongo package
import requests
import pymongo
from pymongo import MongoClient

class dal:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    def getHost(self):
        return self.host
    def getPort(self):
        return self.port

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

def updaterecipes():
    docs_inserted = 0
    duplicate_records = 0
    for doc in datajson:
        try:
            col_match = 0
            for x in client.test.testrecipes.find({},{'sys_id' : 1}):
                if doc['sys_id'] == x['sys_id']:
                    col_match += 1

            if col_match == 0:
                client.test.testrecipes.insert(doc)
                docs_inserted +=1
            if col_match > 0:
                duplicate_records +=1

        except pymongo.errors.DuplicateKeyError:
            continue

    print(str(docs_inserted) + ' document(s) inserted.')
    print(str(duplicate_records)+ ' duplicate record(s)')

updaterecipes()
