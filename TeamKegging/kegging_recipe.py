# Project: Brewing Automation System - Capstone Project
# Purpose Details: Kegging_recipe Class
# Course: IST 440W - 001
# Author: Team Kegging
# Date Developed: 3/23
# Last Date Changed:3/23
# Rev

class Recipe:
    def __init__(self, recipe_id, recipe_volume, recipe_bitter_units, recipe_keg_style, recipe_carbonation):
        self.recipe_id = recipe_id
        self.recipe_volume = recipe_volume
        self.recipe_bitter_units = recipe_bitter_units
        self.recipe_keg_style = recipe_keg_style
        self.recipe_carbonation = recipe_carbonation

    def __str__(self):
        return self.name