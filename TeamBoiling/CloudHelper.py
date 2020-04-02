# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: David Karminski(dck5200@psu.edu)
# Date Developed: 3/18/20
# Last Date Changed: 3/31/20
# Rev 1

class CloudHelper():

    # _local_database = Database
    _database_type = ""
    _database_count = 1

    def __init__(self):
        #self._local_database
        self._database_type
        self._database_count

    def __init__(self, _database_type, _database_count, _local_database):
        '''
        Overloaded constructor method to initialize parameter and access attributes
        :param _database_type: type of database to know where data is going
        :param _database_count: counts the database
        :param _local_database: local database
        '''
        self._database_type = _database_type
        self._database_count = _database_count
        self._local_database = _local_database

    def get_database(self):
        '''
        Calls the data from the database
        :return: returns the local database
        '''
        return self._local_database

    def send_database(self):
        '''
        Sends data to the database
        :return: returns the data to send to the database
        '''
        return self.send_database()
