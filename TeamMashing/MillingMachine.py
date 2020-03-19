# Project: Brewing Project
# Purpose Details: Automate milling machine process
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 3/18/2020
# Rev: 1.1

import sys
import datetime
from Log import Log

class MillingMachine:  #MillingMachine Start
    def __init__(self, mid, mt): #constructor initalized fields
        self.machine_id = mid
        self.mill_time = mt
        self.is_milled = False
        self.is_transferred = False

    def mill_grains(self): #Mill_grains process start
        try:
            log = Log(1, "Mashing.Milling", "Milling Started", datetime.datetime.now(), "pass")
            print(log.generate_log())
            #mill grains
            log = Log(2, "Mashing.Milling", "Milling Ended", datetime.datetime.now(), "pass")
            print(log.generate_log())
            return "Grains milled"
        except Exception as e: #error handling
            print(e)
    def move_motor(self):
        #move motor
        return "Motor moving"
    def stop_motor(self):
        #stop motor
        return "Motor stopped"