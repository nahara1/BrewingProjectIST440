# Project: Brewing Automation System - Capstone Project
# Purpose Details:
# Course: IST 440W - 001
# Author: Antonio Rivera :)
# Date Developed: 4/14/20
from Brewing import Recipe
from Brewing import BrewBatch
from Brewing import BrewBatchStage
import datetime
from Brewing import Log
import sys

class get_recipe:
    '''
     Pulls data from ServiceNow to add to attributes above
    '''
    import requests

    '''
    Recipe table from Service Now
    '''
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/sc_request?sysparm_query=stage%3DRequested&sysparm_fields=sys_id%2Crequested_for%2Copened_by%2Csys_created_by%2Cdelivery_address%2Cprice%2Cnumber%2Crequest_state%2Cstage&sysparm_limit=1'

    '''
    Log in info.
    '''
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

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(data)

def get_recipe(recipe_name):
    '''
        imports request from service now
    '''
    import requests

    '''
    Set the request parameters
    '''
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_recipe?sysparm_query=recipe_name%3D' + recipe_name + '&sysparm_limit=1'

    '''
    Initializing data variable
    '''
    data = ''

    '''
    Set connection success boolean to false
    '''
    connection_success = False

    '''
    Set proper headers
    '''
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    while not connection_success:
        try:
            response = requests.get(url, auth=(user, pwd), headers=headers)
            data = response.json()
        except requests.HTTPError:
            time.sleep(5)
            print('Connection Error')
        else:
            connection_success = True

    print()

    print("json recipe data: " + str(data))
    print()
    def extract_values(obj, key):
        """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

    recipe_obj = extract_values(data, 'sys_id')
    recipe_id = str(recipe_obj).replace("['", "").replace("']", "")

    recipe_obj = extract_values(data, 'recipe_name')
    recipe_name = str(recipe_obj).replace("['", "").replace("']", "")

    recipe_obj = extract_values(data, 'batch_size')
    batch_size = str(recipe_obj).replace("['", "").replace("']", "")

    recipe_obj = extract_values(data, 'yeast_amount')
    yeast_amt = str(recipe_obj).replace("['", "").replace("']", "")

    recipe_obj = extract_values(data, 'yeast')
    yeast = str(recipe_obj).replace("['", "").replace("']", "")

    # Grain type and amount stored as name-value pairs
    recipe_obj = extract_values(data, 'grain_bill')
    grain = str(recipe_obj).replace("['", "").replace("']", "")
    print(grain)

    recipe_obj = extract_values(data, 'water_temperature')
    water_temp = str(recipe_obj).replace("['", "").replace("']", "")

    recipe_obj = extract_values(data, 'water_volume')
    water_volume = str(recipe_obj).replace("['", "").replace("']", "")

    # Stored as name-value pairs
    recipe_obj = extract_values(data, 'hop_schedule')
    hop_schedule = str(recipe_obj).replace("['", "").replace("']", "")

    # Stored as name-value pairs
    recipe_obj = extract_values(data, 'hop_hop_amt')
    hop_amt = str(recipe_obj).replace("['", "").replace("']", "")



    '''
    Creates recipe object
    '''
    recipe_obj = Recipe.Recipe(recipe_id, recipe_name, batch_size, yeast_amt, yeast, grain,
                               water_volume, water_temp, hop_schedule, hop_amt,)

    print(),
    print("Recipe data successfully retrieved")
    return recipe_obj
