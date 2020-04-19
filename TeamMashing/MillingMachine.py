# Project: Brewing Project
# Purpose Details: Automate milling machine process
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 4/18/2020
# Rev: 2.0

import datetime
import time

from Brewing.Log import Log
from TeamMashing.HotLiquorTank import HotLiquorTank
from Brewing.ServiceNowLog import ServiceNowLog

class MillingMachine():  # MillingMachine Start
    def __init__(self):  # constructor initalized fields
        self.machine_id = 1
        self.mill_time = 0
        self.grains_weight = 0

    def mill_grains(self, recipe, request_number):  # Mill_grains process start
        """
        The start of milling grains
        :param request_number:
        :param recipe: recipe instance
        :param mid: machine id
        :param mt: milling time
        :return: Return Log and animation of milling grains
        """
        self.mill_time = recipe.get_mill_time()
        self.grains_weight = recipe.get_grain_weight(recipe.get_grain())

        try:
            # log to begin process
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Starting Mashing Process\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(2, "Mashing.Milling", "Milling Started", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------")

            while self.mill_time > 0:
                print("Milling Time Left: ", self.mill_time, "min")
                time.sleep(1)
                self.mill_time -= 1

                if self.mill_time == 0:
                    print("Grains milled")
                    print("-----------------------------------------")

            # log to end process
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Milling Ended\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(2, "Mashing.Milling", "Milling Ended", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------")
            self.send_grains_to_sparging_tank(recipe, request_number)
        except Exception as e:  # error handling
            print(e)

    def send_grains_to_sparging_tank(self, recipe, request_number):
        # sends grains to Sparging Tank
        """
        grains are added to the Sparging Tank
        :param
        :return: print statement
        """
        try:
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Mashing\", \"log\":\"Sending Grains to Sparging Tank\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(3, "Mashing.Milling", "Send Grains to Sparging Tank", datetime.datetime.now(), "pass")
            print(log.generate_log())
            print("-----------------------------------------")

            print("Grains added to Sparging Tank")
            print("-----------------------------------------")
            hlt = HotLiquorTank()
            hlt.heat_water(recipe, request_number)
        except Exception as e:
            print(e)