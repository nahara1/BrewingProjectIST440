# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for implementing quality assurance
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/18/20
# Last Date Changed: 4/18/2020
# Rev 10

# Import Statements
import time
import logging
from Brewing import ServiceNowLog
from time import sleep


class QualityCheck:
    # Variables
    _sanitization = bool
    _read_temp = float
    _read_weight_grains = float
    _read_weight_hops = float
    _read_weight_sugar = float

    def __init__(self, _sanitization, _read_temp, _read_weight_grains, _read_weight_hops, _read_weight_sugar):

        logging.info("Thread %s: starting QACheck", self)  # Threading
        self._sanitization = _sanitization
        self._read_temp = _read_temp
        self.read_weight_grains = _read_weight_grains
        self.read_weight_hops = _read_weight_hops
        self.read_weight_sugar = _read_weight_sugar
        logging.info("Thread %s: finishing QACheck for Prep", self)  # Threading

    '''
    defines all the getters and setters 
    '''
    logging.info("Thread %s: starting Getters and Setters")  # Threading

    def get_sanitization(self):

        return self._sanitization

    def set_recipe_boil_temp(self, _sanitization):

        self._sanitization = _sanitization

    def get_read_temp(self):

        return self._read_temp

    def set_read_temp(self, _read_temp):

        self._read_temp = _read_temp

    def get_read_weight_grains(self):

        return self._read_weight_grains()

    def set_read_weight_grains(self, _read_weight_grains):

        self._read_weight_grains = _read_weight_grains

    def get_read_weight_hops(self):

        return self._read_weight_hops()

    def set_read_weight_hops(self, _read_weight_hops):

        self._read_weight_hops = _read_weight_hops

    def get_read_weight_sugar(self):

        return self._read_weight_hops()

    def set_read_weight_sugar(self, _read_weight_sugar):

        self._read_weight_sugar = _read_weight_sugar

    logging.info("Thread %s: finishing Getters and Setters for Prep")  # Threading
'''
interface of the QA including variations (yes/no)
'''
def get_QA_Check(self):
        print("Please Inspect the Prep Quality Before Start Brewing to Check if it Meets CGMP Standards: \n")
        # save text as variable
        quality_checked = ""
        while quality_checked != "Yes" or quality_checked != "No":
            if quality_checked == "Yes":
                print("Logging to ServiceNow...")
                sleep(1)
                status_log = "{\"batch_id\":\"1\", \"brew_batch_stage\":\"Preparation\", \"log\":\"Finished Prep process; Passed QA\"}"
                ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
                sleep(1)
                print("Successfully logged that Prep processes has completed and passes Quality Assurance.")
                sleep(1)
                break
            elif quality_checked == "No":
                print("Logging to ServiceNow...")
                sleep(1)
                status_log = "{\"batch_id\":\"1\", \"brew_batch_stage\":\"Preparation\", \"log\":\"Prep stage; Failed QA\"}"
                ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
                sleep(1)
                print("Quality Did not Pass, make correction and inspect again.")
                quality_checked = ""
                sleep(1)
            else:
                text = input("Please Enter Yes or No: ")
                quality_checked = text


QualityCheck: QualityCheck = QualityCheck('_sanitization', '_temperature', '_read_weight_grains', '_read_weight_hops',
                                          '_read_weight_sugar')
# QualityCheck.get_QA_Check()
