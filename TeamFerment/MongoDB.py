# Project: MongoDB - Barlog Brewery
# Purpose Details: Stores all logging information of application runs.
# Course: IST 440
# Author: Team Ferment
# Date Developed: 3/18/2020
# Last Date Changed: 4/2/2020
# Rev: 2


import sys, datetime
from pymongo import MongoClient

"""
  The contents printed are needed to connect to the Local Host, and to provide logging messages, confirming 
  the recipe has been retrieved. 
"""


def connectToDB():
    client = MongoClient('localhost', 27017)
    db = client['TeamFerment']
    collection_log = db['logMessages']

# def mongoInstance(typer, text, self):
#    try:
#        post = {
#            "type": typer, "text": text, "date": datetime.datetime.utcnow()
#                }
#        post_id = self.collection.insert_one(post)

