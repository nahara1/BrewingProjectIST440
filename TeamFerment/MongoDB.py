# Project: MongoDB - Barlog Brewery
# Purpose Details: Stores all logging information of application runs.
# Course: IST 440
# Author: Jinal Parmar
# Date Developed: 3/18/2020
# Last Date Changed: 3/22/2020


import sys, datetime
from pymongo import MongoClient


def connectToDB():
    client = MongoClient('localhost', 27017)
    db = client.dbTeamFerment
    collection = db.logMessages

# def mongoInstance(typer, text):
#    try:
#       post = {"type": typer,
#               "text": text,
#               "date": datetime.datetime.utcnow()}
# post_id = self.collection.insert_one(post)
