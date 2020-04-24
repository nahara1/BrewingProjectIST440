# Project: Brewing Project
# Purpose Details: Automate Hot Liquor Tank Process
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 4/23/2020
# Rev: 4.0

import datetime
from Brewing.Log import Log
from TeamMashing.SpargingTank import SpargingTank
from Brewing.ServiceNowLog import ServiceNowLog
from Brewing import MongoLogging


class HotLiquorTank:
    def __init__(self):
        self.tank_ID = 2
        self.water_amount = 0
        self.water_temp = 0

    def heat_water(self, recipe, request_number):  # Water heating process starts

        """
        The start of water heating
        :param request_number:
        :param recipe: a recipe instance
        :return: return log and animation of burner light.
        """

        self.water_amount = recipe.get_water_volume()
        self.water_temp = recipe.get_water_temp()

        try:
            # log to begin process
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Water heating\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(1, "Mashing.HotLiquorTank", "Water heating started.", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------")

            print("Water Temperature Heated To: ", self.water_temp, " degrees F")
            print("-----------------------------------------")

            ml = MongoLogging.MongoLogging()
            MongoLogging.MongoLogging.MongoLog(ml, request_number, "Mashing.HotLiquorTank", "Water heating started")

            self.check_water_temp(recipe, request_number)

        except Exception as e:
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Water Heating Failed\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(1, "Mashing.Milling", "Water Heating Failed", datetime.datetime.now(), "fail")
            print(log.generate_log())
            print("-----------------------------------------")
            ml = MongoLogging.MongoLogging()
            MongoLogging.MongoLogging.MongoLog(ml, request_number, "Mashing.HotLiquorTank", "Water Heating Failed")
            print(e)

    def check_water_temp(self, recipe, request_number):
        """
        Checks the current temperature of the water.
        :return: current water temperature
        """
        try:
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Checking Water Temp\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(2, "Mashing.HotLiquorTank", "Checking Water Temperature", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------")

            print("Water Temperature: ", self.water_temp, "degrees F")
            print("-----------------------------------------")

            ml = MongoLogging.MongoLogging()
            MongoLogging.MongoLogging.MongoLog(ml, request_number, "Mashing.HotLiquorTank", "Checking Water Temperature")

            self.check_water_volume(recipe, request_number)

        except Exception as e:
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Checking Water Temperature Failed\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(1, "Mashing.HotLiquorTank", "Checking Water Temperature", datetime.datetime.now(), "fail")
            print(log.generate_log())
            print("-----------------------------------------")

            ml = MongoLogging.MongoLogging()
            MongoLogging.MongoLogging.MongoLog(ml, request_number, "Mashing.HotLiquorTank","Water Temperature Failed")
            print(e)

    def check_water_volume(self, recipe, request_number):
        """
        Getter for water volume
        :return: water volume.
        """
        try:
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Checking Water Volume\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(3, "Mashing.HotLiquorTank", "Checking Water Volume", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------")

            print("Water Volume: ", self.water_amount, "gallons")
            print("-----------------------------------------")

            ml = MongoLogging.MongoLogging()
            MongoLogging.MongoLogging.MongoLog(ml, request_number, "Mashing.HotLiquorTank","Checking Water Volume")

            self.send_hot_water_to_sparging_tank(recipe, request_number)

        except Exception as e:
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Checking Water Volume Failed\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(1, "Mashing.HotLiquorTank", "Checking Water Volume Failed", datetime.datetime.now(), "fail")
            print(log.generate_log())
            print("-----------------------------------------")
            ml = MongoLogging.MongoLogging()
            MongoLogging.MongoLogging.MongoLog(ml, request_number, "Mashing.HotLiquorTank","Checking Water Volume Failed")
            print(e)


    def send_hot_water_to_sparging_tank(self, recipe, request_number):
        """

        :return: print statement
        """
        try:
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Sending Hot Water to Sparging Tank\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(3, "Mashing.HotLiquorTank", "Sending Hot Water to Sparging Tank", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------")

            print("Hot water is sent to Sparging Tank.")
            print("-----------------------------------------")

            ml = MongoLogging.MongoLogging()
            MongoLogging.MongoLogging.MongoLog(ml, request_number, "Mashing.HotLiquorTank","Hot water is sent to Sparging Tank")

            st = SpargingTank()
            st.add_water(recipe, request_number)
        except Exception as e:
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Sending Hot Water to Sparging Tank Failed\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(1, "Mashing.HotLiquorTank", "Sending Hot Water to Sparging Tank Failed", datetime.datetime.now(),
                      "fail")
            print(log.generate_log())
            print("-----------------------------------------")

            ml = MongoLogging.MongoLogging()
            MongoLogging.MongoLogging.MongoLog(ml, request_number, "Mashing.HotLiquorTank","Sending Hot Water to Sparging Tank Failed")

            print(e)
