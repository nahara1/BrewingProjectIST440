# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Nahara (nkm5334)
# Date Developed: 4/14/20
# Last Date Changed: 4/15/20
# Rev 1

from Brewing import Recipe

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



def get_brew_request_number(req_id):
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/sc_request/' + req_id

    import requests
    '''
    number = REQ number
    sys_created_by = logged user
    STAGE = STATUS (NEEDS TO BE UPDATED THROUGH PROCESS)

    opened_by 
    '''
    # Eg. User name="admin", Password="admin" for this code sample.
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

    username = extract_values(response.json(), 'sys_created_by')

    username = str(username).replace("['", "").replace("']", "")

    request_number = extract_values(response.json(), 'number')

    request_number = str(request_number).replace("['", "").replace("']", "")

    print("Customer User ID: " + username)

    print()

    print("Brew Request Number: " + request_number)

    data = response.json()

    return request_number


def get_request_id():
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/sc_request?sysparm_query=stage%3DRequested&sysparm_fields=sys_id%2Crequested_for%2Copened_by%2Csys_created_by%2Cdelivery_address%2Cprice%2Cnumber%2Crequest_state%2Cstage&sysparm_limit=1'

    import requests
    '''
    number = REQ number
    sys_created_by = logged user
    STAGE = STATUS (NEEDS TO BE UPDATED THROUGH PROCESS)

    opened_by 
    '''
    # Eg. User name="admin", Password="admin" for this code sample.
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

    sys_id = extract_values(response.json(), 'sys_id')

    sys_id = str(sys_id).replace("['", "").replace("']", "")

    return sys_id


# get_brew_request()


def get_catalog_item_id(request_number):
    import requests

    # Set the request parameters

    '''

    value in request is the sys_id of request record in sc_request table
    request:
    value = sys_id in sc_request

    cat_item:
    value = item sys_id in cat_item table

    '''
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/sc_req_item?sysparm_query=request.number%253D' + request_number + '&sysparm_limit=1' + '&sysparm_fields=sys_id%2Cnumber%2Ccat_item&sysparm_limit=10'
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
    cat_item_id = extract_values(data, 'value')
    cat_item_id = str(cat_item_id).replace("['", "").replace("']", "")
    # print("Catalog Item ID: " + cat_item_id)
    return cat_item_id


def get_catalog_item_name(cat_id):
    import requests

    # Set the request parameters
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/sc_cat_item/' + cat_id + '?sysparm_fields=sys_name'

    # Eg. User name="admin", Password="admin" for this code sample.
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
    recipe_name = extract_values(data, 'sys_name')
    recipe_name = str(recipe_name).replace("['", "").replace("']", "")
    print("Requested Brew Name: " + recipe_name)
    return recipe_name


# def get_recipe(item_name):


def update_brew_stage(sys_id, stage):
    import requests
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/sc_request/' + sys_id
    # Eg. User name="admin", Password="admin" for this code sample.
    user = 'IST440'
    pwd = 'IST440'

    # Set proper headers
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    # Do the HTTP request
    update = "{\"stage\":\"" + stage + "\"}"

    # updates requests table
    response = requests.patch(url, auth=(user, pwd), headers=headers, data=update)

    # Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.json())
        exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    print()
    print("Brew Stage Updated")
    print()


def get_recipe(recipe_name):
    import requests

    # Set the request parameters
    url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_recipe?sysparm_query=recipe_name%3D' + recipe_name + '&sysparm_limit=1'

    # Eg. User name="admin", Password="admin" for this code sample.
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
    print()
    print("json recipe data: " + str(data))
    print()

    ''' create a recipe object '''
    # TODO - Add ALL recipe variables
    recipe_obj = extract_values(data, 'sys_id')
    recipe_id = str(recipe_obj).replace("['", "").replace("']", "")
    recipe_obj = extract_values(data, 'recipe_name')
    recipe_name = str(recipe_obj).replace("['", "").replace("']", "")
    recipe_obj = extract_values(data, 'batch_size')
    batch_size = str(recipe_obj).replace("['", "").replace("']", "")
    recipe_obj = extract_values(data, 'yeast')
    yeast = str(recipe_obj).replace("['", "").replace("']", "")
    recipe_obj = extract_values(data, 'abv')
    abv = str(recipe_obj).replace("['", "").replace("']", "")
    recipe_obj = extract_values(data, 'ibu')
    ibu = str(recipe_obj).replace("['", "").replace("']", "")
    recipe_obj = extract_values(data, 'og')
    og = str(recipe_obj).replace("['", "").replace("']", "")
    recipe_obj = extract_values(data, 'fg')
    fg = str(recipe_obj).replace("['", "").replace("']", "")
    recipe_obj = extract_values(data, 'grain_bill')
    grain_bill = str(recipe_obj).replace("['", "").replace("']", "")
    recipe_obj = extract_values(data, 'water_temperature')
    water_temperature = str(recipe_obj).replace("['", "").replace("']", "")
    recipe_obj = extract_values(data, 'water_volume')
    water_volume = str(recipe_obj).replace("['", "").replace("']", "")
    recipe_obj = extract_values(data, 'sparging_time')
    sparging_time = str(recipe_obj).replace("['", "").replace("']", "")
    recipe_obj = extract_values(data, 'boiling_duration')
    boiling_duration = str(recipe_obj).replace("['", "").replace("']", "")

    recipe = Recipe.Recipe(recipe_id, recipe_name, batch_size, yeast, abv, ibu, og, fg)
    print(recipe)
    print("Recipe data successfully retrieved")
    return recipe


if __name__ == "__main__":

    # Get a brew request

    # 1 - Get brew request id
    r_id = get_request_id()

    # 2 - Get brew request number
    r_number = get_brew_request_number(r_id)

    # 3 - Update brew request
    update_brew_stage(r_id, "Approval")

    # 4 - Get requested brew id based on request number
    item_id = get_catalog_item_id(r_number)

    # 5 - Get requested item name based on its id
    item_name = get_catalog_item_name(item_id)

    # 6 - Get recipe data and create a Python object based on brew request name
    get_recipe(item_name)

    # 7 - Update brew request status
    update_brew_stage(r_id, "Preparation Stage")