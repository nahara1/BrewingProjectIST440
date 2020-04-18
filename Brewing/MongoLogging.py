# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for logging to MongoDB
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 4/16/20
# Last Date Changed: 4/16/2020
# Rev 1

from pymongo import MongoClient
import datetime


class MongoLogging():

    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client.logging_database
    collection = db.logging_collection

    post = {"BrewID": "1",
            "Brew Stage": "Prep",
            "Log": "Began Prep",
            "date": datetime.datetime.utcnow()}

    posts = db.posts
    post_id = posts.insert_one(post).inserted_id

    db.list_collection_names()

