# GET
# Reading records from ServiceNow and saving them into local mongo database
from pymongo import MongoClient
import pymongo
from json import loads
from collections import OrderedDict



client = MongoClient('localhost', 27017)
db = client['recipes_db']
collection_recipe = db['recipes']
#GET request w/ database table fields specified
#Need to install requests package for python
#easy_install requests
import requests, json, ast, itertools
# Set the request parameters
'''
Use sysparm_fields=field_name => field_name is the field you want to read
separate fields using commas in case you want to read more than one field from a table
'''
url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_recipe?sysparm_fields=sys_id%2Crecipe_name%2Ctype%2Cstyle%2Cog%2Cfg%2Cabv%2Cibu%2Cwater_volume%2Cwater_temperature%2Cgrain_bill%2Cboiling_duration%2Cyeast&sysparm_limit=100'
#Use IST440 for both user and pwd
user = 'IST440'
pwd = 'IST440'
# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}
# Do the HTTP request
# GET is the request to read data
response = requests.get(url, auth=(user, pwd), headers=headers )

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(type(data))
print()
print("This is a json dictionary: ", data, "Type: ", type(data))

# No we need to get the list of key value pairs from our dict
print()
#json.load(data, object_pairs_hook=OrderedDict)
recipe_names_pairs = data['result']

print("This is a list: ", recipe_names_pairs)
print()
# Check type
print("Recipe_names_pairs is of the list type and can now be used to create documents in mongddb: " , type(recipe_names_pairs))
print()
#db.collection_recipe.insert(recipe_names_pairs)

# For loop to iterate through the key value pairs obtained from the json response
# and a try catch block to check if any has previously been inserted in the collection
for doc in recipe_names_pairs:
    try:
        # insert into db collection
        print("Inserting ",  doc, " into db...")
        message = "Inserting ",  doc, " into db..."
        db.collection_recipe.insert_one(doc)
    except pymongo.errors.DuplicateKeyError:
        # skip document because it already exists in the local db collection
        continue