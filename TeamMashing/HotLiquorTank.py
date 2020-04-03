# Project: Brewing Project
# Purpose Details: Automate Hot Liquor Tank Process
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 3/24/2020
# Rev: 1.1

import sys
import datetime
import time
from Log import Log


class HotLiquorTank:
    def __init__(self, tID, wVolume, wtemperature):
        self.tank_ID = tID
        self.water_amount = wVolume
        self.water_temp = wtemperature
        self.is_transferred = False

    def heat_water(self): #Water heating process starts

        """
        The start of water heating
        :param tID: tank ID
        :param wVolume: volume of water
        :param wtemperature: temperature of the water
        :param istransferred: transfer indication
        :return: return log and animation of burner light.
        """

        try:
            # log to begin process
            log = Log(1, "Mashing.HotLiquorTank", "Water heating started.", datetime.datetime.now(), "pass")
            print(log.generate_log())

            # log to end process
            log = Log(2, "Mashing.HotLiquorTank", "Water heating completed.", datetime.datetime.now(), "pass")
            print(log.generate_log())
            return "Water temperature correct."

        except Exception as e:
            print(e)

    def get_tank_ID(self):
        """
        This gets the tank ID.
        :return: tID
        """
        return self.tID

    def get_water(self):
        """
        Getter for water volume
        :return: water volume.
        """
        return self.wVolume

    def send_hot_water(self):
        """
        
        :return:
        """
        return ("Hot water is sent.")

    def check_water_temp(self):
        """
        Checks the current temperature of the water.
        :return: current water temperature
        """
        return self.wtemperature