# Project: Brewing Automation System - Capstone Project
# Purpose Details: Class to get a brew request
# Course: IST 440W - 001
# Author: Nahara (nkm5334)
# Date Developed: 4/14/20
# Last Date Changed: 4/24/20
# Rev 6

"""
This module handles the retrieval of brew request data from ServiceNow
"""

from Brewing import Recipe

import time
import ast

# Set user authentication for HTTP requests
user = 'IST440'
pwd = 'IST440'


# Function to work with nested JSON
# Code from: https://hackersandslackers.com/extract-data-from-complex-json-python/

def extract_values(obj, key):
    """
    Extracts values from a nested json given a specific key
    :param obj: a json payload
    :param key: any key present in the nested json payload
    :return: a value of the given key
    """
    arr = []

    def extract(obj, arr, key):
        """
        Recursively searches for a key in a nested json payload and appends its value to an array.

        :param obj: a json payload
        :param arr: an array to store nested key-value pairs
        :param key: a key present in the given json payload
        :return: an array of key-value pairs
        """

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


def get_request_id():
    """
    Retrieves a brew request id from the ServiceNow requests table
    :return: request_id
    """
    # Requests Table url
    #url = 'https://emplkasperpsu2.service-now.com/api/now/table/sc_request?sysparm_query=stage%3DRequested&sysparm_fields=sys_id%2Crequested_for%2Copened_by%2Csys_created_by%2Cdelivery_address%2Cprice%2Cnumber%2Crequest_state%2Cstage&sysparm_limit=1'
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/sc_request?sysparm_query=stageLIKERequested&sysparm_limit=1'

    import requests

    # Initialize the row id of a record in ServiceNow
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
            sys_id = extract_values(data, 'sys_id')
            sys_id = str(sys_id).replace("['", "").replace("']", "")

    except requests.HTTPError:
        time.sleep(5)
        print('Connection Error')
        get_request_id()

    return sys_id


# Method to get a request number (which will be used a the brew batch id)

def get_brew_request_number(req_id):
    """
    Gets the brew order request number corresponding to the request id given
    :param req_id: brew request unique row identifier
    :return: brew request number
    """

    # Set url based on the given request ID
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/sc_request/' + req_id

    import requests

    # Set connection to false until the HTTP request is successful
    connection_success = False

    # Set proper headers
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    # Initialize data variable
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

    # Get ServiceNow username of the customer who placed the brew request
    username = extract_values(data, 'sys_created_by')

    username = str(username).replace("['", "").replace("']", "")

    # Get the request number
    request_number = extract_values(data, 'number')

    request_number = str(request_number).replace("['", "").replace("']", "")

    print("Customer User ID: " + username)

    print()
    print("Brew Request Number: " + request_number)

    return request_number


def get_catalog_item_id(request_number):
    """
    Gets the catalog item unique identifier which has been requested by a customer
    based on the given request number

    :param request_number: a brew request order number
    :return: ServiceNow Catalog Item ID
    """
    import requests

    # Set the request parameters
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/sc_req_item?sysparm_query=requestLIKE' + request_number + '&sysparm_limit=1' + '&sysparm_fields=sys_id%2Cnumber%2Ccat_item'

    # Set connection to false until the HTTP request is successful
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
    cat_item_id = extract_values(data, 'value')
    print("cat id: ", cat_item_id)
    cat_item_id = str(cat_item_id).replace("['", "").replace("']", "")
    # print("Catalog Item ID: " + cat_item_id)
    return cat_item_id


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

    # Set connection to false until the HTTP request is successful
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

    # Set the recipe name to the name of the catalog item that was requested
    recipe_name = extract_values(data, 'sys_name')
    recipe_name = str(recipe_name).replace("['", "").replace("']", "")
    print("Requested Brew Name: " + recipe_name)
    return recipe_name


def update_brew_stage(sys_id, stage):
    """
    Updates the request Stage column in the sc_request table
    As teh brew batch passes along each brew stage, this method will be called to updated the stage
    of the corresponding brew request
    :param sys_id: unique identifier of a brew request
    :param stage: Brew Batch current stage
    """
    import requests
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/sc_request/' + sys_id

    # Set stage value to be patched
    update = "{\"stage\":\"" + stage + "\"}"

    # Set connection to false until the HTTP request is successful
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
    Gets all recipe fields in the ServiceNow table given a recipe name.
    Each recipe value is retrieved and parsed into a string and into an integer or float,
    and then a Recipe object is created out of those values.

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
    # Call extract_values method and pass in teh json payload and the specific column name
    # to create variables for the each column parsing them into a string and into an integer
    # float depending on the variable

    # Get row id of the recipe record
    recipe_obj = extract_values(data, 'sys_id')
    recipe_id = str(recipe_obj).replace("['", "").replace("']", "")

    # Get recipe name variable from the given recipe
    recipe_obj = extract_values(data, 'recipe_name')
    recipe_name = str(recipe_obj).replace("['", "").replace("']", "")

    # Get recipe name variable from the given recipe
    recipe_obj = extract_values(data, 'batch_size')
    batch_size = str(recipe_obj).replace("['", "").replace("']", "")
    batch_size = int(batch_size)

    # Get abv variable from the given recipe
    recipe_obj = extract_values(data, 'abv')
    abv = str(recipe_obj).replace("['", "").replace("']", "")
    abv = float(abv)

    # Get ibu variable from the given recipe
    recipe_obj = extract_values(data, 'ibu')
    ibu = str(recipe_obj).replace("['", "").replace("']", "")
    # Parse ibu into an integer
    ibu = int(ibu)

    # Get ibu variable from the given recipe
    recipe_obj = extract_values(data, 'og')
    og = str(recipe_obj).replace("['", "").replace("']", "")
    # Parse og into a float
    og = float(og)

    # Get fg variable from the given recipe
    recipe_obj = extract_values(data, 'fg')
    fg = str(recipe_obj).replace("['", "").replace("']", "")
    # Parse fg into a float
    fg = float(fg)

    # Get yeast amount from the given recipe
    recipe_obj = extract_values(data, 'yeast_amount')
    yeast_amt = str(recipe_obj).replace("['", "").replace("']", "")
    # Parse yeast amount into an integer
    yeast_amt = int(yeast_amt)

    # Get yeast from the given recipe
    recipe_obj = extract_values(data, 'yeast')
    yeast = str(recipe_obj).replace("['", "").replace("']", "")

    # Grain type and amount are stored as name-value pairs
    # Get grains from the given recipe
    recipe_obj = extract_values(data, 'grain_bill')
    grain = str(recipe_obj).replace("['", "").replace("']", "")
    # Convert name-value pairs into a Python dictionary
    grain = ast.literal_eval(grain)

    # Get water temperature from the given recipe
    recipe_obj = extract_values(data, 'water_temperature')
    water_temp = str(recipe_obj).replace("['", "").replace("']", "")
    # Parse water temperature into an integer
    water_temp = int(water_temp)

    # Get water volume from the given recipe
    recipe_obj = extract_values(data, 'water_volume')
    water_volume = str(recipe_obj).replace("['", "").replace("']", "")
    # Parse water volume into an integer
    water_volume = int(water_volume)

    # Get mill time from the given recipe
    recipe_obj = extract_values(data, 'mill_time')
    mill_time = str(recipe_obj).replace("['", "").replace("']", "")
    # Parse mill time into an integer
    mill_time = int(mill_time)

    # Get sparge time from the given recipe
    recipe_obj = extract_values(data, 'sparging_time')
    sparge_time = str(recipe_obj).replace("['", "").replace("']", "")
    # Parse sparge time into an integer
    sparge_time = int(sparge_time)

    # Get stir time from the given recipe
    recipe_obj = extract_values(data, 'stir_time')
    stir_time = str(recipe_obj).replace("['", "").replace("']", "")
    # Parse stir time into an integer
    stir_time = int(stir_time)

    # Get HLT heating time from the given recipe
    recipe_obj = extract_values(data, 'hlt_heating_time')
    hlt_heat_time = str(recipe_obj).replace("['", "").replace("']", "")
    # Parse HLT heat time into an integer
    hlt_heat_time = int(hlt_heat_time)

    # Get wort separation time from the given recipe
    recipe_obj = extract_values(data, 'wort_separation_time')
    wort_separation_time = str(recipe_obj).replace("['", "").replace("']", "")
    # Parse wort separation time into an integer
    wort_separation_time = int(wort_separation_time)

    # Get wort volume from the given recipe
    recipe_obj = extract_values(data, 'wort_volume')
    wort_volume = str(recipe_obj).replace("['", "").replace("']", "")
    # Parse wort volume into an integer
    wort_volume = int(wort_volume)

    # Get boil temperature from the given recipe
    recipe_obj = extract_values(data, 'boil_temperature')
    boil_temp = str(recipe_obj).replace("['", "").replace("']", "")
    # Parse boil temperature into an integer
    boil_temp = int(boil_temp)

    # Get boiling duration from the given recipe
    recipe_obj = extract_values(data, 'boiling_duration')
    boil_duration = str(recipe_obj).replace("['", "").replace("']", "")
    # Parse boil duration into an integer
    boil_duration = int(boil_duration)

    # Hop schedule is stored as name-value pairs
    recipe_obj = extract_values(data, 'hop_schedule')
    hop_schedule = str(recipe_obj).replace("['", "").replace("']", "")
    # Convert string into a dictionary
    hop_schedule = ast.literal_eval(hop_schedule)

    # The amount is stored as name-value pairs
    recipe_obj = extract_values(data, 'hop_hop_amount')
    hop_amt = str(recipe_obj).replace("['", "").replace("']", "")
    # Convert string into a dictionary
    hop_amt = ast.literal_eval(hop_amt)

    # Get wort chill temperature from the given recipe
    recipe_obj = extract_values(data, 'wort_chill_temperature')
    wort_chill_temp = str(recipe_obj).replace("['", "").replace("']", "")
    # Parse wort chill temp into a float
    wort_chill_temp = float(wort_chill_temp)

    # Get ferment duration from the given recipe
    recipe_obj = extract_values(data, 'ferment_duration')
    ferment_time = str(recipe_obj).replace("['", "").replace("']", "")
    # Parse ferment time into an integer
    ferment_time = int(ferment_time)

    # Get ferment temperature from the given recipe
    recipe_obj = extract_values(data, 'ferment_temperature')
    ferment_temp = str(recipe_obj).replace("['", "").replace("']", "")
    # ferment_temp = float(ferment_temp)

    # Create recipe object
    recipe_obj = Recipe.Recipe(recipe_id, recipe_name, abv, ibu, og, fg, batch_size, yeast_amt, yeast, grain,
                               water_volume, water_temp, mill_time, sparge_time,
                               stir_time, hlt_heat_time, wort_separation_time, boil_temp, boil_duration, hop_schedule,
                               hop_amt,
                               wort_chill_temp, ferment_time, ferment_temp, wort_volume)

    print()
    print("Recipe data successfully retrieved")
    return recipe_obj
