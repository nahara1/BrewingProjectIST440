# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for logging to MongoDB
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 4/16/20
# Last Date Changed: 4/16/2020
# Rev 1

from pymongo import MongoClient
import datetime


class MongoLogging:

    def MongoLog(self,log):
        """
        method that adds a log to the MongoDB Collection
        :param log: preformated string in JSON format to log to MongoDB
        :return: none
        """
        try:
            print("Attempting to connect to MongoDB...")
            client = MongoClient('localhost', 27017)
            db = client.logging_database
            collection = db.logging_collection
        except Exception as e:
            print("MongoDB connection Error:" + str(e))

        try:
            for x in collection.find({}, {'sys_id': 1}):
                print(x)
                if log['sys_id'] == x['sys_id']:
                    print()
                    print('sys_id duplicate - no document inserted')
                else:
                    client.test.testrecipes.insert(log)
                    print('document inserted')
        except Exception as e2:
            print("Duplicate Key Error" + str(e2))

    #post = {"BrewID": "1",
    #        "Brew Stage": "Prep",
    #        "Log": "Began Prep",
    #        "date": datetime.datetime.utcnow()}

    #posts = db.posts
    #post_id = posts.insert_one(post).inserted_id

    #db.list_collection_names()

