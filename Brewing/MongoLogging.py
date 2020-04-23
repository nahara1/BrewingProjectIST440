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

    def MongoLog(self, request_number, process, log_message):
        """
        method that adds a log to the MongoDB Collection
        :param log: preformated string in JSON format to log to MongoDB
        :return: none
        """
        try:
            print("Attempting to connect to MongoDB...")
            client = MongoClient('localhost', 27017)
            db = client.database
            collection = db.logging_database

            status_log = {"Request_No": request_number, "Brewing_Process": process, "Log_Message": log_message, "Time": datetime.datetime.now()}

            collection.insert_one(status_log)

            print(status_log)
        except Exception as e:
            print("MongoDB connection Error:" + str(e))