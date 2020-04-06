# Project: Brewing Automation System - Capstone Project
# Purpose Details: class assisting with connecting and saving to the local database
# Course: IST 440W - 001
# Author: David Karminski(dck5200@psu.edu)
# Date Developed: 3/18/20
# Last Date Changed: 4/1/20
# Rev 1

class DBHelper():

    _db_type = ""
    _db_name = ""
    _db_connection = ""

    def __init__(self):
        self._db_type
        self. _db_name
        self._db_connection

    def __init__(self, _db_type, _db_name, _db_connection):
        '''
        Overloads Constructor method to create methods and access attributes
        :param _db_type: database type
        :param _db_name: name of the database
        :param _db_connection: connects to the database
        '''
        self._db_type = _db_type
        self._db_name = _db_name
        self._db_connection = _db_connection

    def get_db_type(self):
        '''
        Calls the database to get the type
        :return: returns the database type
        '''
        return self._db_type

    def get_db_name(self):
        '''
        Calls the database to get the name of it
        :return: returns the name of the database
        '''
        return self._db_name

    def get_db_connection(self):
        '''
        Establishes the database connection
        :return: returns the database connection
        '''
        return self._db_connection

    def save_database(self):
        '''
        Saves the database if data is added or changed
        :return: returns the save to the database
        '''
        return self.save_database()

    def send_database(self):
        '''
        Sends data to the database
        :return: returns the sent data to the database
        '''
        return self.send_database

    def connect_to_network(self):
        '''
        Connects to the network for connection with database
        :return: returns the network connection
        '''
        return self.connect_to_network

