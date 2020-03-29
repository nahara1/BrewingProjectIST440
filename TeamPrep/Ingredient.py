# Project: Brewing Automation System - Capstone Project
# Purpose Details: Creation of the Ingredients
# Course: IST 440W - 001
# Author: Chris Parks
# Date Developed: Design Phase
# Last Date Changed: 3/29/2020


class Ingredients():
    def __init__(self, ID,  quanity, weight):
        self.ID = ID
        self.quanity = quanity
        self.weight = weight
        def __int__(self):
            return (self.ID, self.quanity, self.weight)
class Yeast(Ingredients):
    def __init__(self, temp):
        self.temp = temp
        super().__init__(ID = {}, quanity = {}, weight = {})
        def __float__(self):
            return self.temp
class Grain(Ingredients):
    def __init__(self):
        super().__init__(ID = {}, quanity = {}, weight = {})
class Hop(Ingredients):
    def __init__(self):
        super().__init__(ID = {}, quanity = {}, weight = {})
class Sugar(Ingredients):
    def __init__(self):
        super().__init__(ID = {}, quanity = {}, weight = {})




