# Project: Brewing Project
# Purpose Details: Sparging tank transfer and automation
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 4/15/2020
# Rev: 1.5
import datetime
import time
from Brewing.MongoLog import Log
from TeamMashing.Wort import Wort
from TeamMashing.RecipeMashing import recipe_mashing

class SpargingTank: #constructor for the SpargingTank class
    def __init__(self):
        self.machine_id = 3
        self.stir_time = recipe_mashing.stir_time
        self.heating_time = recipe_mashing.heating_time
        self.water_amount = recipe_mashing.water_amount
        self.water_temp = recipe_mashing.water_temp
        self.sparging_time = recipe_mashing.sparging_time

    def add_water(self):
        #adding heated water to tank
        """
        Water added to tank from hot liquor tank (HLT)
        :param :Hot water from HLT
        :return: Return log 1
        """
        try:
            log = Log(1, "Mashing.Sparging", "Heated water added to tank", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------") # prints line to separate statements & log 1 is created

            print("Water Temp: ", self.water_temp, "degrees F") # displays water temp in degrees F
            print("Added Heated Water to Sparging Tank") # print validates the process of water being heated
            print("-----------------------------------------") # prints line to separate the next process in sparging tank

            self.stir_mash()
        except Exception as e:
            print(e)

    def stir_mash(self):
        #stirring the wort in progress
        """
        Function to stirr the Wort-in progress sparging tank
        :param : Wort in HLT
        :param : time.sleep is pausing the process for 1 second
        :return: Return log 2
        """
        try:
            log = Log(2, "Mashing.Sparging", "Sparging Process Started", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------") # prints line to separate statements & log 2 is created

            while self.stir_time > 0:
                print("Stirring Time Left: ", self.stir_time, "sec") # prints number of seconds left until stirring is
                # finished
                time.sleep(1)
                self.stir_time -= 1

                if self.stir_time == 0:
                    print ("SpargingTank stirred") # print validates that SpargingTank is finished stirring


            log = Log(3, "Mashing.Sparging", "Sparging Process Ended", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------") # prints line to separate statements & log 3 is created

            print("Mash Stirred") # print that the mashing is finished stirring
            print("-----------------------------------------") # prints line to separate process within SpargingTank
            self.sparg_the_tank()
        except Exception as e:
            print(e)


    def sparg_the_tank(self):
        #empty the tank while spraying water over the remaing grains
        """
        Function to remove finished wort from Sparging tank.
        :param : Wort in HLT
        :return: Return log 4
        """
        try:
            log = Log(4, "Mashing.Sparging", "Mash Sparged to Boiling", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------") # prints line to separate statements & log 4 is created

            print("Tank emptying, washing grains.") # Finishing before sending it to the boiling phase
            print("-----------------------------------------")
            w = Wort()
            w.check_hot_water_temp()
        except Exception as e:
            print(e)