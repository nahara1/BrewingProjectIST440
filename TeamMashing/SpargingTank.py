# Project: Brewing Project
# Purpose Details: Sparging tank transfer and automation
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 4/21/2020
# Rev: 3.0
import datetime
import time
from Brewing.Log import Log
from TeamMashing.Wort import Wort
from Brewing.ServiceNowLog import ServiceNowLog

class SpargingTank: #constructor for the SpargingTank class
    def __init__(self):
        self.machine_id = 3
        self.stir_time = 0
        self.water_temp = 0

    def add_water(self, recipe, request_number):
        try:
            #adding heated water to tank
            """
            Water added to tank from hot liquor tank (HLT)
            :param :Hot water from HLT
            :return: Return log 1
            """

            self.water_temp = recipe.get_water_temp()

            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Adding Hot Water to Tank\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(1, "Mashing.Sparging", "Heated water added to tank", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------") # prints line to separate statements & log 1 is created

            print("Water Temp: ", self.water_temp, "degrees F") # displays water temp in degrees F
            print("Added Heated Water to Sparging Tank") # print validates the process of water being heated
            print("-----------------------------------------") # prints line to separate the next process in sparging tank

            self.stir_mash(recipe, request_number)
        except Exception as e:
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Adding Hot Water to Tank Failed\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(1, "Mashing.Sparging", "Adding Hot Water to Tank Failed", datetime.datetime.now(), "fail")
            print(log.generate_log())
            print("-----------------------------------------")
            print(e)

    def stir_mash(self, recipe, request_number):
        #stirring the wort in progress
        """
        Function to stirr the Wort-in progress sparging tank
        :param : Wort in HLT
        :param : time.sleep is pausing the process for 1 second
        :return: Return log 2
        """
        try:
            self.stir_time = recipe.get_stir_time()

            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Stirring Mash\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(2, "Mashing.Sparging", "Sparging Process Started", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------") # prints line to separate statements & log 2 is created

            while self.stir_time > 0:
                print("Stirring Time Left: ", self.stir_time, "min") # prints number of seconds left until stirring is
                # finished
                time.sleep(1)
                self.stir_time -= 1

                if self.stir_time == 0:
                    print ("SpargingTank stirred") # print validates that SpargingTank is finished stirring
                    print("-----------------------------------------")

            status_log = "{\"batch_id\":\"" + request_number + "\",\"brew_batch_stage\":\"Mashing\",\"log\":\"Mash Stirred\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(3, "Mashing.Sparging", "Sparging Process Ended", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------") # prints line to separate statements & log 3 is created

            print("Mash Stirred") # print that the mashing is finished stirring
            print("-----------------------------------------") # prints line to separate process within SpargingTank
            self.sparg_the_tank(recipe, request_number)
        except Exception as e:
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Mashing Stirred Failed\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(1, "Mashing.Sparging", "Mashing Stirred Failed", datetime.datetime.now(), "fail")
            print(log.generate_log())
            print("-----------------------------------------")
            print(e)

    def sparg_the_tank(self, recipe, request_number):
        #empty the tank while spraying water over the remaing grains
        """
        Function to remove finished wort from Sparging tank.
        :param : Wort in HLT
        :return: Return log 4
        """
        try:
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Sparging the Tank\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(4, "Mashing.Sparging", "Sparging the Tank", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------") # prints line to separate statements & log 4 is created

            print("Tank emptying, washing grains.") # Finishing before sending it to the boiling phase
            print("-----------------------------------------")
            w = Wort()
            w.check_hot_water_temp(recipe, request_number)
        except Exception as e:
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Sparging the Tank Failed\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(1, "Mashing.Sparging", "Sparging the Tank Failed", datetime.datetime.now(), "fail")
            print(log.generate_log())
            print("-----------------------------------------")
            print(e)
