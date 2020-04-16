# Project: Brewing Project
# Purpose Details: Automate wort process.
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 4/15/2020
# Rev: 1.5

import datetime
import time
from Brewing.MongoLog import Log
from TeamMashing.RecipeMashing import recipe_mashing

# Wort class checks for water temperature, water volume and records separation time.
class Wort:
    def __init__(self):
        self.wort_id = 4
        self.wort_volume = recipe_mashing.wort_volume
        self.hot_water_temp = recipe_mashing.water_temp
        self.water_volume = recipe_mashing.water_amount
        self.separation_time = recipe_mashing.separation_time

    def check_hot_water_temp(self):
        # Checks for water temperature
        """
        Displays correct water temp in the wort phase / generates a log
        :return: Displays current date, time and correct water temperature
        """
        # Records correct hot water temp to Log
        try:
            log = Log(1, "Mashing.Wort", "Wort transferred", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------")

            print("Hot Water Temperature: ", self.hot_water_temp, "degrees F")
            print("-----------------------------------------")

            self.check_water_volume()
        except Exception as e:
            print(e)

    def check_water_volume(self):
        # Checks for water volume
        """
        Displays the correct water volume / generates a log
        :return: Current date, time and correct water volume
        """
        try:
            log = Log(2, "Mashing.Wort", "Water Volume", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------")

            print("Water Volume: ", self.water_volume, "gallons")
            print("-----------------------------------------")

            self.check_wort_volume()
        except Exception as e:
            print(e)

    def check_wort_volume(self):    # Wort Volume? Should we use it as BatchSize
        # Displays wort volume
        """
        Displays the correct wort volume / generates a log
        :return: Current date, time and correct wort volume / and a log
        """
        # Records correct wort volume to Log and show animation
        try:
            log = Log(3, "Mashing.Wort", "Wort Transferred", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------")

            print("Wort Volume: ", self.wort_volume, "gallons")
            print("-----------------------------------------")

            self.separate_wort()
        except Exception as e:
            print(e)

    def separate_wort(self):
        # Separates the wort from the mash
        """
        Displays a count down while wort separation is in process
        :return: Current date, time and count down to separating wort.
        """
        try:
            log = Log(4, "Mashing.Wort", "Wort Separation Started", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------")

            # Counts the separation time in seconds
            while self.separation_time > 0:
                print("Wort Separating Time Left: ", self.separation_time, "sec")
                time.sleep(1)
                self.separation_time -= 1

                # Verifies that the wort separation has been completed.
                if self.separation_time == 0:
                    print("Wort Separation Completed")
                    print("-----------------------------------------")

            # Generates a log and displays the process has been successfully completed.
            log = Log(5, "Mashing.Wort", "Wort Separation Ended", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------")

            print("Wort Separated from Mash")
            print("-----------------------------------------")
        except Exception as e:  # error handling
            print(e)
