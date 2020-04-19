# Project: Brewing Automation System - Capstone Project
# Purpose Details: Class to get a brew request
# Course: IST 440W - 001
# Author: Nahara (nkm5334)
# Date Developed: 4/14/20
# Last Date Changed: 4/18/20
# Rev 5
"""
This module handles the retrieval of brew request data from ServiceNow
"""

from Brewing import Recipe
from Brewing import BrewBatch
from Brewing import BrewBatchStage
import datetime
from Brewing import Log
import sys

import time
import ast
user = 'IST440'
pwd = 'IST440'


# Function to work with nested JSON
# Code from: https://hackersandslackers.com/extract-data-from-complex-json-python/

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


# method to get a new request id

def get_request_id():
    """
    Retrieves the most recent brew request id from the ServiceNow requests table
    :return: request_id
    """
    # table url
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/sc_request?sysparm_query=stage%3DRequested&sysparm_fields=sys_id%2Crequested_for%2Copened_by%2Csys_created_by%2Cdelivery_address%2Cprice%2Cnumber%2Crequest_state%2Cstage&sysparm_limit=1'

    import requests
    '''
    number = REQ number
    sys_created_by = logged user
    STAGE = STATUS (NEEDS TO BE UPDATED THROUGH PROCESS)

    opened_by 
    '''
    sys_id = ''
    # Set proper headers
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    try:
        # Do the HTTP request
        response = requests.get(url, auth=(user, pwd), headers=headers)
        data = response.json()

        if str(data) == "{'result': []}":
            time.sleep(5)
            print("No brew request available at this time.")
            print()
            get_request_id()

        else:
            # Decode the JSON response into a dictionary and use the data
            req_id = extract_values(data, 'sys_id')
            req_id = str(sys_id).replace("['", "").replace("']", "")

    except requests.HTTPError:
        time.sleep(5)
        print('Connection Error')
        get_request_id()

    return req_id


# method to get a request number (which will be used a the brew batch id)

def get_brew_request_number(req_id):
    """
    Get the order request number corresponding to the request id given
    :param req_id: brew request unique identifier
    :return: brew batch id request number
    """
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/sc_request/' + req_id

    import requests
    '''
    number = REQ number
    sys_created_by = logged user
    STAGE = STATUS (NEEDS TO BE UPDATED THROUGH PROCESS)

    opened_by 
    '''

    connection_success = False
    # Set proper headers
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    data = ''

    while not connection_success:
        try:
            response = requests.get(url, auth=(user, pwd), headers=headers)
            data = response.json()

        except requests.HTTPError:
            time.sleep(5)
            print('Connection Error')
            print()

        # Do the HTTP request
        else:
            connection_success = True

    username = extract_values(data, 'sys_created_by')

    username = str(username).replace("['", "").replace("']", "")

    brew_batch_id = extract_values(data, 'number')

    brew_batch_id = str(brew_batch_id).replace("['", "").replace("']", "")

    print("Customer User ID: " + username)

    print()
    print("Brew Request Number: " + brew_batch_id)

    return brew_batch_id


def get_catalog_item_id(brew_batch_id):
    """
    Get the catalog item unique identifier which has been requested by a customer
    based on the given request number

    :param request_number: a brew request order number
    :return: ServiceNow Catalog Item ID
    """
    import requests

    '''
    Value in request is the sys_id of request record in the sc_request table
    request id:
    value = sys_id in sc_request

    cat_item:
    value = catalog item sys_id in the cat_item table

    '''
    # Set the request parameters
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/sc_req_item?sysparm_query=request.number%253D' + brew_batch_id + '&sysparm_limit=1' + '&sysparm_fields=sys_id%2Cnumber%2Ccat_item'

    connection_success = False

    # Set proper headers
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    while not connection_success:
        try:
            response = requests.get(url, auth=(user, pwd), headers=headers)

        except requests.HTTPError:
            time.sleep(5)
            print('Connection Error')
        else:
            connection_success = True

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    cat_id = extract_values(data, 'value')
    print(cat_id)
    cat_id = str(cat_id).replace("['", "").replace("']", "")
    # print("Catalog Item ID: " + cat_item_id)
    return cat_id


def get_catalog_item_name(cat_id):
    """
    Get catalog item name given its id, which corresponds to a recipe name in the Recipe table.

    :param cat_id: Catalog Item Unique Identifier
    :return: a catalog item name
    """
    import requests

    # Set the request parameters
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/sc_cat_item/' + cat_id + '?sysparm_fields=sys_name'

    # Initialize data variable
    data = ""

    # Set connection to false
    connection_success = False

    # Set proper headers
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    while not connection_success:
        try:
            response = requests.get(url, auth=(user, pwd), headers=headers)
            data = response.json()

        except requests.HTTPError:
            time.sleep(5)
            print('Connection Error')

        # Do the HTTP request
        else:
            connection_success = True

    recipe_name = extract_values(data, 'sys_name')
    recipe_name = str(recipe_name).replace("['", "").replace("']", "")
    print("Requested Brew Name: " + recipe_name)
    return recipe_name


def update_brew_stage(request_id, stage):
    # Stage is a string
    """
    Update request Stage column in the sc_request table
    As teh brew batch passes along each brew stage, this method will be called to updated the stage
    of the corresponding brew request
    :param sys_id: unique identifier of a brew request
    :param stage: Brew Batch current stage
    """
    import requests
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/sc_request/' + request_id

    # Set stage value to be patched
    update = "{\"stage\":\"" + stage + "\"}"

    connection_success = False

    # Set proper headers
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    while not connection_success:
        try:
            # Update requests table
            response = requests.patch(url, auth=(user, pwd), headers=headers, data=update)

        except requests.HTTPError:
            time.sleep(5)
            print('Connection Error')

        else:
            connection_success = True

    print("\nBrew Stage Updated\n")


def get_recipe(recipe_name):
    """
    Get all recipe fields in the SNow table given a recipe name.
    Each recipe value is retrieved and parsed into a string, and then a Recipe object is created out of those values.

    :param recipe_name: The name of a recipe, also the name of the catalog item
    :return: a Recipe object
    """
    import requests

    # Set the request parameters
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_recipe?sysparm_query=recipe_name%3D' + recipe_name + '&sysparm_limit=1'

    # Initializing data variable
    data = ''

    # Set connection success boolean to false
    connection_success = False

    # Set proper headers
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

    # Create a Recipe Object based on the record retrieved from the SNow Recipe table
    recipe_obj = extract_values(data, 'sys_id')
    recipe_id = str(recipe_obj).replace("['", "").replace("']", "")

    recipe_obj = extract_values(data, 'recipe_name')
    recipe_name = str(recipe_obj).replace("['", "").replace("']", "")

    recipe_obj = extract_values(data, 'batch_size')
    batch_size = str(recipe_obj).replace("['", "").replace("']", "")
    batch_size = int(batch_size)

    recipe_obj = extract_values(data, 'abv')
    abv = str(recipe_obj).replace("['", "").replace("']", "")
    abv = float(abv)

    recipe_obj = extract_values(data, 'ibu')
    ibu = str(recipe_obj).replace("['", "").replace("']", "")
    ibu = int(ibu)

    recipe_obj = extract_values(data, 'og')
    og = str(recipe_obj).replace("['", "").replace("']", "")
    og = float(og)

    recipe_obj = extract_values(data, 'fg')
    fg = str(recipe_obj).replace("['", "").replace("']", "")
    fg = float(fg)

    recipe_obj = extract_values(data, 'yeast_amount')
    yeast_amt = str(recipe_obj).replace("['", "").replace("']", "")
    yeast_amt = int(yeast_amt)

    recipe_obj = extract_values(data, 'yeast')
    yeast = str(recipe_obj).replace("['", "").replace("']", "")

    # recipe_obj = extract_values(data, 'yeast_initial_temperature')
    # yeast_initial_temp = str(recipe_obj).replace("['", "").replace("']", "")

    # Grain type and amount stored as name-value pairs
    recipe_obj = extract_values(data, 'grain_bill')
    grain = str(recipe_obj).replace("['", "").replace("']", "")
    grain = ast.literal_eval(grain)

    recipe_obj = extract_values(data, 'water_temperature')
    water_temp = str(recipe_obj).replace("['", "").replace("']", "")
    water_temp = int(water_temp)

    recipe_obj = extract_values(data, 'water_volume')
    water_volume = str(recipe_obj).replace("['", "").replace("']", "")
    water_volume = int(water_volume)

    recipe_obj = extract_values(data, 'mill_time')
    mill_time = str(recipe_obj).replace("['", "").replace("']", "")
    mill_time = int(mill_time)

    recipe_obj = extract_values(data, 'sparging_time')
    sparge_time = str(recipe_obj).replace("['", "").replace("']", "")
    sparge_time = int(sparge_time)

    recipe_obj = extract_values(data, 'stir_time')
    stir_time = str(recipe_obj).replace("['", "").replace("']", "")
    stir_time = int(stir_time)

    recipe_obj = extract_values(data, 'hlt_heating_time')
    hlt_heat_time = str(recipe_obj).replace("['", "").replace("']", "")
    hlt_heat_time = int(hlt_heat_time)

    recipe_obj = extract_values(data, 'wort_separation_time')
    wort_separation_time = str(recipe_obj).replace("['", "").replace("']", "")
    wort_separation_time = int(wort_separation_time)

    recipe_obj = extract_values(data, 'wort_volume')
    wort_volume = str(recipe_obj).replace("['", "").replace("']", "")
    wort_volume = int(wort_volume)

    recipe_obj = extract_values(data, 'boil_temperature')
    boil_temp = str(recipe_obj).replace("['", "").replace("']", "")
    boil_temp = int(boil_temp)

    recipe_obj = extract_values(data, 'boiling_duration')
    boil_duration = str(recipe_obj).replace("['", "").replace("']", "")
    boil_duration = int(boil_duration)

    # Stored as name-value pairs
    recipe_obj = extract_values(data, 'hop_schedule')
    hop_schedule = str(recipe_obj).replace("['", "").replace("']", "")

    # Stored as name-value pairs
    recipe_obj = extract_values(data, 'hop_hop_amt')
    hop_amt = str(recipe_obj).replace("['", "").replace("']", "")

    recipe_obj = extract_values(data, 'wort_chill_temperature')
    wort_chill_temp = str(recipe_obj).replace("['", "").replace("']", "")
    #wort_chill_temp = float(wort_chill_temp)

    recipe_obj = extract_values(data, 'ferment_duration')
    ferment_time = str(recipe_obj).replace("['", "").replace("']", "")
    ferment_time = int(ferment_time)

    recipe_obj = extract_values(data, 'ferment_temperature')
    ferment_temp = str(recipe_obj).replace("['", "").replace("']", "")
    #ferment_temp = float(ferment_temp)

    recipe_obj = extract_values(data, 'ferment_yeast_temp')
    ferment_yeast_temp = str(recipe_obj).replace("['", "").replace("']", "")
    #ferment_yeast_temp = float(ferment_yeast_temp)


    # Create recipe object
    recipe_obj = Recipe.Recipe(recipe_id, recipe_name, abv, ibu, og, fg, batch_size, yeast_amt, yeast, grain,
                               water_volume, water_temp, mill_time, sparge_time,
                               stir_time, hlt_heat_time, wort_separation_time, boil_temp, boil_duration, hop_schedule, hop_amt,
                               wort_chill_temp, ferment_time, ferment_temp, ferment_yeast_temp, wort_volume)


    print()
    print("Recipe data successfully retrieved")
    return recipe_obj
