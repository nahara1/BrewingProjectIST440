# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for logging to MongoDB
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 4/16/20
# Last Date Changed: 4/16/2020
# Rev 1

from pymongo import MongoClient
import datetime


class dal:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port


class MongoLogging:

    def MongoLog(self, log):
        """
        method that adds a log to the MongoDB Collection
        :param log: preformated string in JSON format to log to MongoDB
        :return: none
        """
        dalHandler = dal('localhost', 27017)
        # Connection to MongoDB
        try:
            client = MongoClient(dalHandler.getHost(), dalHandler.getPort())
            # Select the Database
            db = client.logging_database
            # Select the Collection
            collection = db.logging_collection
            # Select one Document
        except Exception as e:
            print("Cannot connect to the MongoDB" + str(e))

        try:
            client.logging_database.logging_collection.insert(log)
        except Exception as e2:
            print("Duplicate Key Error" + str(e2))


status_log = "{\"batch_id\":\"" + str(
    1234) + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Starting Mashing Process\"}"
m1 = MongoLogging()
m1.MongoLog(status_log)
