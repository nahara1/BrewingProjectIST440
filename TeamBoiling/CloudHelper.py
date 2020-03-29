# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: David Karminski(dck5200@psu.edu)
# Date Developed: 3/18/20
# Last Date Changed:
# Rev 1


class CloudHelper():

    # _local_database = Database
    _database_type = ""
    _database_count = 1

    def __init__(self):
        # self._local_database
        self._database_type
        self._database_count

    def __init__(self, _database_type, _database_count, _local_database):
        self._database_type = _database_type
        self._database_count = _database_count
        self._local_database = _local_database

    def get_database(self):
        return self._local_database

    def send_database(self):
        return self.send_database()
