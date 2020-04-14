# Project: Brewing Automation System - Capstone Project
# Purpose Details: Creation of the Ingredients
# Course: IST 440W - 001
# Author: Chris Parks
# Date Developed: Design Phase
# Last Date Changed: 4/6/2020


class Ingredients:

    def __init__(self, ID, quantity, weight):
        self.ID = ID
        self.quantity = quantity
        self.weight = weight
        '''
        defines the attributes for the ingredients 
        '''
        self.ID = int
        self.quantity = int
        self.weight = float
        '''
        Adds the methods to the attributes for the ingredients 
        '''
class Yeast(Ingredients):
    def __init__(self, temp):
        self.temp = temp
        temp = float
        '''
        Added the temperature attribute with the yeast class with the method
        '''
        super().__init__(ID={""}, quantity={""}, weight={""})

        def __float__(self):
            return self.temp
        '''
        adds the attributes for the yeast 
        '''
        print(Yeast)

        '''
       prints out a list of the attributes listed for the yeast abstract class with data that goes along with the recipe pulled from the ServiceNow table
       '''

class Grain(Ingredients):
    def __init__(self):
        super().__init__(ID={""}, quantity={""}, weight={""})
        '''
        adds the attributes for the grains
        '''

        print(Grain)

        '''
       prints out a list of the attributes listed for the grain abstract class with data that goes along with the recipe pulled from the ServiceNow table
       '''

class Hop(Ingredients):
    def __init__(self):
        super().__init__(ID={""}, quantity={""}, weight={""})
        '''
        adds the attributes for the hops
        '''

        print(Hop)
    '''
    prints out a list of the attributes listed for the hop abstract class with data that goes along with the recipe pulled from the ServiceNow table
    '''
class Sugar(Ingredients):
    def __init__(self):
        super().__init__(ID={""}, quantity={""}, weight={""})
        '''
        adds the attributes for the sugar
        '''
        print(Sugar)
    '''
    prints out a list of the attributes listed for the sugar abstract class with data that goes along with the recipe pulled from the ServiceNow table
    '''

class Water(Ingredients):
    def __init__(self):
            super().__init__(quantity={""})
    '''
    adds the attributes for the water
    '''
print(Water)
'''
prints out  the attribute listed for the water abstract class with data that goes along with the recipe pulled from the ServiceNow table
'''

class get_ingredient:
    '''
    This class will pull data from ServiceNow to add to the attributes listed above
    '''
    # Need to install requests package for python
    # easy_install requests
    import requests

    # Set the request parameters
    url = ''

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
    print(data)