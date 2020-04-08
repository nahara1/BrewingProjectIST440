# Project: Brewing Project
# Purpose Details: Created for each team to log into the mongo database
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 3/18/2020
# Rev: 1.1

import sys
import time
class Log:
    def __init__(self, lid, bs, l, lt, pof): #contructor initializes fields
        self.log_id = lid
        self.brewstage = bs
        self.log = l
        self.log_time = lt
        self._passOrFail = pof

    def generate_log(self): #method generates a log in a readable format
        return "LogID: {}\n" \
            "Brew Stage: {}\n" \
            "Log: {}\n" \
            "Log Time: {}\n" \
            "Pass or Fail: {}\n".format(self.log_id, self.brewstage, self.log, self.log_time, self._passOrFail)