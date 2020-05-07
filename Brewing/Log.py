# Project: Brewing Project
# Purpose Details: Created for each team to log into the mongo database
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 3/18/2020
# Rev: 1.1

import sys
import time
import sys

class Log:
    def __init__(self, lid, brew_stage, log, log_time, pass_or_fail):  # constructor initializes fields
        """
        Log constructor that initializes fields
        :param lid: log id
        :param brew_stage: brew batch stage
        :param log: log message
        :param log_time: log time
        :param pass_or_fail: log status
        """
        self.log_id = lid
        self.brew_stage = brew_stage
        self.log = log
        self.log_time = log_time
        self.pass_or_fail = pass_or_fail

    def generate_log(self):  # method generates a log in a readable format
        """
        Generates a log in readable format
        :return: a readable log
        """

        return "Brew Stage: {}\n" \
               "Log: {}\n" \
               "Log Time: {}\n" \
               "Pass or Fail: {}\n".format(self.brew_stage, self.log, self.log_time, self.pass_or_fail)
