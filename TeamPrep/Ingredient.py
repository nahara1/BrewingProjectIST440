# Project: Brewing Automation System - Capstone Project
# Purpose Details: Creation of the Ingredients
# Course: IST 440W - 001
# Author: Chris Parks
# Date Developed: Design Phase
# Last Date Changed: 4/6/2020


class Ingredients:

    def __init__(self, ID, quantity, weight):
        """
        Ingredients Constructor that defines the attributes for the ingredients
        :param ID: ingredient ID
        :param quantity: ingredient quantity
        :param weight: ingredient weight
        """
        self.ID = ID
        self.quantity = quantity
        self.weight = weight

        self.ID = int
        self.quantity = int
        self.weight = float


class Yeast(Ingredients):
    """
    Extend Ingredients Class
    """

    def __init__(self, temp):
        """
        Yeast Constructor
        Prints out a list of the attributes listed for the yeast class with data
        that goes along with the recipe pulled from the ServiceNow table
        :param temp: yeast temperature
        """
        self.temp = temp
        temp = float
        super().__init__(ID={""}, quantity={""}, weight={""})

        def __float__(self):
            return self.temp

        print(Yeast)


class Grain(Ingredients):
    def __init__(self):
        """
        Grain Constructor
        Defines the attributes for the grains
        Prints out a list of the attributes listed for the grain abstract class with
        data that goes along with the recipe pulled from the ServiceNow table
        """
        super().__init__(ID={""}, quantity={""}, weight={""})

        print(Grain)


class Hop(Ingredients):
    """
    Hop Constructor
    Defines the attributes for the hops and prints out a list of the attributes
    listed for the hop class with the data that comes from the recipe record
    pulled from the ServiceNow table
    """

    def __init__(self):
        super().__init__(ID={""}, quantity={""}, weight={""})

        print(Hop)


class Sugar(Ingredients):
    """
    Sugar Constructor
    Defines the attributes for the sugar and prints them out data that comes
    from recipe record pulled from the ServiceNow table
    """

    def __init__(self):
        super().__init__(ID={""}, quantity={""}, weight={""})
        print(Sugar)


class Water(Ingredients):
    """
    Water Constructor
    Defines the attributes for the water
    """

    def __init__(self):
        super().__init__(quantity={""})
