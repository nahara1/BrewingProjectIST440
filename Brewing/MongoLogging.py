# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for logging to MongoDB
# Course: IST 440W - 001
# Author: Team Boiling
# Date Developed: 4/16/20
# Last Date Changed: 4/23/2020
# Rev 2

from pymongo import MongoClient
import datetime


class MongoLogging:

    def MongoLog(self, request_number, process, log_message):
        """
        method that adds a log to the MongoDB Collection
        :param log_message:
        :param process:
        :param request_number:
        :param log_message: preformed string in JSON format to log to MongoDB
        :return: none
        """
        try:
            print("Attempting to connect to MongoDB...")
            client = MongoClient('localhost', 27017)
            db = client.database
            collection = db.logging_database

            status_log = {"Request_No": request_number, "Brewing_Process": process, "Log_Message": log_message,
                          "Time": datetime.datetime.now()}

            try:
                collection.insert_one(status_log)
            except TypeError:  # Error Handling for MongoDB versions that do not implement insert_one() method
                collection.insert(status_log)

            print(status_log)
        except Exception as e:
            print("MongoDB connection Error:" + str(e))
