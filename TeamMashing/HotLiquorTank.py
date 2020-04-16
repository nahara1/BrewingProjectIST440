# Project: Brewing Project
# Purpose Details: Automate Hot Liquor Tank Process
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 4/15/2020
# Rev: 1.4

import datetime
from Brewing.MongoLog import Log
from TeamMashing.SpargingTank import SpargingTank
from TeamMashing.RecipeMashing import recipe_mashing

class HotLiquorTank:
    def __init__(self):
        self.tank_ID = 2
        self.water_amount = recipe_mashing.water_amount
        self.water_temp = recipe_mashing.water_temp

    def heat_water(self): #Water heating process starts

        """
        The start of water heating
        :param water_temp: temperature of the water
        :return: return log and animation of burner light.
        """

        try:
            # log to begin process
            log = Log(1, "Mashing.HotLiquorTank", "Water heating started.", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------")

            print("Water Temperature Heated To: ", self.water_temp, " degrees F")
            print("-----------------------------------------")

            self.check_water_temp()

        except Exception as e:
            print(e)

    def check_water_temp(self):
        """
        Checks the current temperature of the water.
        :return: current water temperature
        """
        try:
            log = Log(2, "Mashing.HotLiquorTank", "Checking Water Temperature", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------")

            print("Water Temperature: ", self.water_temp, "degrees F")
            print("-----------------------------------------")

            self.check_water_volume()

        except Exception as e:
            print(e)

    def check_water_volume(self):
        """
        Getter for water volume
        :return: water volume.
        """
        try:
            log = Log(3, "Mashing.HotLiquorTank", "Checking Water Volume", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------")

            print("Water Volume: ", self.water_amount, "gallons")
            print("-----------------------------------------")

            self.send_hot_water_to_sparging_tank()

        except Exception as e:
            print(e)

    def send_hot_water_to_sparging_tank(self):
        """
        
        :return: print statement
        """
        try:
            log = Log(3, "Mashing.HotLiquorTank", "Sending Hot Water to Sparging Tank", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------")

            print("Hot water is sent to Sparging Tank.")
            print("-----------------------------------------")

            st = SpargingTank()
            st.add_water()
        except Exception as e:
            print(e)
