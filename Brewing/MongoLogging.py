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

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def MongoLog(self, log):
        """
        method that adds a log to the MongoDB Collection
        :param log: preformated string in JSON format to log to MongoDB
        :return: none
        """
        try:
            print("Attempting to connect to MongoDB...")
            #client = MongoClient('localhost', 27017)
            db = self.logging_database
            collection = db.logging_collection
        except Exception as e:
            print("MongoDB connection Error:" + str(e))

        #try:
            #for x in MongoClient.logging_database.logging_collection.find({}, {'sys_id': 1}):
                #print(x)
                #if log['sys_id'] == x['sys_id']:
                    #print()
                    #print('sys_id duplicate - no document inserted')
                #else:
        MongoClient.logging_database.logging_collection.insert(log)
                    #print('document inserted')
        #except Exception as e2:
            #print("Duplicate Key Error" + str(e2))

    # post = {"BrewID": "1",
    #        "Brew Stage": "Prep",
    #        "Log": "Began Prep",
    #        "date": datetime.datetime.utcnow()}

    # posts = db.posts
    # post_id = posts.insert_one(post).inserted_id

    # db.list_collection_names()

status_log = "{\"batch_id\":\"" + str(1234) + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Starting Mashing Process\"}"
m1 = MongoLogging()
m1.MongoLog(status_log)