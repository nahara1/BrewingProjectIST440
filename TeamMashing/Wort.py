# Project: Brewing Project
# Purpose Details: Automate wort process.
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 3/31/2020
# Rev: 1.3

import datetime
import time
from Brewing.MongoLog import Log

class Wort:
    def __init__(self):
        self.wort_id = 4
        self.wort_volume = 30
        self.hot_water_temp = 140
        self.water_volume = 20
        self.separation_time = 10

    def check_hot_water_temp(self):
        # Sets and displays the correct water temperature
        """
        :param int: displays correct water temp
        :return :Return Log and animation of wort processes
        """
        # Records correct hot water temp to Log and show animation
        log = Log(1, "Mashing.Wort", "Wort transferred", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("-----------------------------------------")

        print("Hot Water Temperature: ", self.hot_water_temp, "degrees F")
        print("-----------------------------------------")

        self.check_water_volume()

    def check_water_volume(self):
        # Displays the correct water volume
        """
        :param current_water_volume: get the correct water volume
        :param set_correct_water_volume: set the correct water volume
        :param :transfer correct water volume
        :return: Return Log and animation of wort processes
        """
        log = Log(2, "Mashing.Wort", "Water Volume", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("-----------------------------------------")

        print("Water Volume: ", self.water_volume, "gallons")
        print("-----------------------------------------")

        self.check_wort_volume()

    def check_wort_volume(self):
        # Sets and displays wort volume
        """
        :type :float
        :param float: shows correct wort volume
        :return: Return log and animation of wort processes
        """
        # Records correct wort volume to Log and show animation
        log = Log(3, "Mashing.Wort", "Wort Transferred", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("-----------------------------------------")

        print("Wort Volume: ", self.wort_volume, "gallons")
        print("-----------------------------------------")

        self.separate_wort()

    def separate_wort(self):
        # Separates the wort from the mash
        """
        :return: Return Log and animation
        """
        log = Log(4, "Mashing.Wort", "Wort Separation Started", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("-----------------------------------------")

        while self.separation_time > 0:
            print("Wort Separating Time Left: ", self.separation_time, "sec")
            time.sleep(1)
            self.separation_time -= 1

            if self.separation_time == 0:
                print("Wort Separation Completed")
                print("-----------------------------------------")

        log = Log(5, "Mashing.Wort", "Wort Separation Ended", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("-----------------------------------------")

        print("Wort Separated from Mash")
        print("-----------------------------------------")
