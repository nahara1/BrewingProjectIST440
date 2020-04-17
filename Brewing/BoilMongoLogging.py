# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for logging to MongoDB
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 4/16/20
# Last Date Changed: 4/16/2020
# Rev 1

import pymongo
from pymongo import MongoClient
import datetime


class BoilMongoLogging():

    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client.test_database
    collection = db.test_collection

    post = {"author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}

    posts = db.posts
    post_id = posts.insert_one(post).inserted_id

    db.list_collection_names()

