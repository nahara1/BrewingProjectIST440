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
    def __init__(self, lid, brew_stage, log, log_time, pass_or_fail):  # constructor initializes fields
        self.log_id = lid
        self.brew_stage = brew_stage
        self.log = log
        self.log_time = log_time
        self.pass_or_fail = pass_or_fail

    def generate_log(self):  # method generates a log in a readable format
        return "LogID: {}\n" \
               "Brew Stage: {}\n" \
               "Log: {}\n" \
               "Log Time: {}\n" \
               "Pass or Fail: {}\n".format(self.log_id, self.brew_stage, self.log, self.log_time, self.pass_or_fail)
