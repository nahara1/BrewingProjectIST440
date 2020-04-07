# Project: Brewing Automation System - Capstone Project
# Purpose Details: Creation of the BrewBatch
# Course: IST 440W - 001
# Author: Chris Parks
# Date Developed: Design Phase
# Last Date Changed: 3/29/2020

class BrewBatch:
    recipe = {}
    current_ingredients = ['yeast', 'grain', 'sugar', 'hops']
    recipe_file = "Ingredient.py"


    with open(recipe_file, 'r') as f:
        for line in f:
            words = line.split()
            if words:
                recipe[words[0]] = words[1:]

    for recipe, ingredients in recipe.items():
        for ingredient in ingredients:
            if ingredient not in current_ingredients:
                break
        else:
            print('You have the ingredients to make: {}'.format(recipe))