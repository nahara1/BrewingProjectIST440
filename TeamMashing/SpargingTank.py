# Project: Brewing Project
# Purpose Details: Sparging tank transfer and automation
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 3/31/2020
# Rev: 1.3
import datetime
import time
from Brewing.MongoLog import Log
from TeamMashing.Wort import Wort


class SpargingTank: #constructor for class sparging tank
    def __init__(self):
        self.machine_id = 3
        self.stir_time = 10
        self.heating_time = 10
        self.water_amount = 20
        self.water_temp = 140
        self.sparging_time = 10

    def add_water(self):
        #adding heated water to tank
        """
        Water added to tank from hot liqor tank
        :param :Hot water from HLT
        :return: Return log and animation
        """
        log = Log(1, "Mashing.Sparging", "Heated water added to tank", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("-----------------------------------------")

        print("Water Temp: ", self.water_temp, "degrees F")
        print("Added Heated Water to Sparging Tank")
        print("-----------------------------------------")

        self.stir_mash()
    def stir_mash(self):
        #stirring the wort in progress
        """
        Function to stirr the Wort-inprogress sparging tank
        :param : Wort in HLT
        :return: Return log and animation
        """
        log = Log(2, "Mashing.Sparging", "Sparging Process Started", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("-----------------------------------------")

        while self.stir_time > 0:
            print("Stirring Time Left: ", self.stir_time, "sec")
            time.sleep(1)
            self.stir_time -= 1

            if self.stir_time == 0:
                print ("SpargingTank stirred")
                print("-----------------------------------------")

        log = Log(3, "Mashing.Sparging", "Sparging Process Ended", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("-----------------------------------------")

        print("Mash Stirred")
        print("-----------------------------------------")
        self.sparg_the_tank()

    def sparg_the_tank(self):
        #empty the tank while spraying water over the remaing grains.
        """
        Function to remove finished wort from Sparging tank.
        :param : Wort in HLT
        :return: Return log and animation
        """
        log = Log(4, "Mashing.Sparging", "Mash Sparged to Boiling", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("-----------------------------------------")

        print("Tank emptying, washing grains.")
        print("-----------------------------------------")
        w = Wort()
        w.check_hot_water_temp()