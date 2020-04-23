# Project: Brewing Automation System - Capstone Project
# Purpose Details: WeightScale Class - To weigh grains, hops and sugar
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/22
# Rev 3


import time
import datetime
from Brewing.Log import Log
from numpy import arange
from Brewing.Recipe import Recipe
from Brewing.ServiceNowLog import ServiceNowLog
from Brewing.BrewRequest import Recipe
from Brewing import MongoLogging


# noinspection PyUnusedLocal,PyMethodMayBeStatic,PyMethodMayBeStatic,PyMethodMayBeStatic
class WeightScale:

    def __init__(self):  # constructor initialized field

        self.log_no = 8
        self.hop_hop_amt = None
        self.grain = None

    # noinspection PyArgumentList,PyArgumentList
    def get_grain(self):
        '''
       Method that gets grain information to prep the weighing process
       Returns: The amount of the grain being used for the weight scale
        '''
        self.grain = Recipe.Recipe.get_grain()
        return self.grain

    # noinspection PyArgumentList,PyArgumentList
    def get_hop_hop_amt(self):
        '''
       Method that gets hops information to prep the weighing process
       Returns: The amount of the hops being used for the weight scale
        '''
        self.hop_hop_amt = Recipe.Recipe.get_hop_hop_amt()
        return self.hop_hop_amt

    # noinspection PyUnboundLocalVariable
    def read_weight_grains(self, recipe, request_number):
        '''
       Method that displays the actual weight of the grains
       Returns: Float of the weight goes into the weight scale with logging to ServiceNOW
        '''
        try:
            grain = list(recipe.grain.keys())
            weight = list(recipe.grain.values())
            weight = list(map(lambda x: float(x.replace(",", "")), weight))
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"WeightScale\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(self.log_no + 1, "Prep.WeightScale", "Grains list and weight copied from ordered brew recipe.",
                      datetime.datetime.now(),
                      "pass")
            print(log.generate_log())
            ml = MongoLogging.MongoLogging()
            MongoLogging.MongoLogging.MongoLog(ml, request_number, "Prep.WeightScale",
                                               "Grains list and weight copied from ordered brew recipe")
            time.sleep(1)
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"WeightScale\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(self.log_no + 1, "Prep.WeightScale", "Hops list and weight copied from ordered brew recipe.",
                      datetime.datetime.now(),
                      "pass")
            print(log.generate_log())
            ml = MongoLogging.MongoLogging()
            MongoLogging.MongoLogging.MongoLog(ml, request_number, "Prep.WeightScale",
                                               "Hops list and weight copied from ordered brew recipe")
            time.sleep(1)
            j = 1

            for i in range(len(grain)):
                weight_scale = 0.0
                status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"WeightScale\"}"
                sn_log = ServiceNowLog()
                ServiceNowLog.create_new_log(sn_log, status_log)
                log = Log(self.log_no + 1, "Prep.WeightScale", "Weight scale is set to zero.",
                          datetime.datetime.now(),
                          "pass")
                print(log.generate_log())
                ml = MongoLogging.MongoLogging()
                MongoLogging.MongoLogging.MongoLog(ml, request_number, "Prep.WeightScale",
                                                   "Weight scale is set to zero")
                time.sleep(1)
                status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"WeightScale\"}"
                sn_log = ServiceNowLog()
                ServiceNowLog.create_new_log(sn_log, status_log)
                log = Log(self.log_no + 1, "Prep.WeightScale", "Brewer is being asked to dispense " + grain[i] + ".",
                          datetime.datetime.now(),
                          "pass")
                print(log.generate_log())
                ml = MongoLogging.MongoLogging()
                MongoLogging.MongoLogging.MongoLog(ml, request_number, "Prep.WeightScale",
                                                   "Brewer is being asked to dispense " + grain[i] + ".")
                time.sleep(1)
                print("    \033[1m3." + str(j) + " To brew the beer for this batch, " + str(weight[i]) + " pounds of " +
                      grain[i]
                      , " needed.\033[0m\n"
                      )
                time.sleep(1)
                print("       ****Weight scale is calibrated to \033[1m0.0\033[0m. \n")
                time.sleep(1)
                input("       Press the Enter to dispense \033[1m" + grain[i] + "\033[0m:\n")

                for weight_scale in arange(float(weight[i])):
                    weight_scale = weight_scale + 1.0
                    time.sleep(1)
                    print("       \033[1m" + str(
                        weight_scale) + "\033[0;0m pound(s) \033[1m" + grain[i] + "\033[0m received. \033[1m" + str(
                        weight[i] - weight_scale) + "\033[0m pound(s) left to be dispensed. \n")
                    time.sleep(1)
                    if float(weight[i]) == weight_scale:
                        print("       \033[1m" + grain[i] + "\033[0m are measured and \033[1m" + str(
                            weight_scale) + "\033[0m pounds received.  \n")
                        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"WeightScale\"}"
                        sn_log = ServiceNowLog()
                        ServiceNowLog.create_new_log(sn_log, status_log)
                        log = Log(self.log_no, "Prep.WeightScale", grain[i] + " grain received.",
                                  datetime.datetime.now(),
                                  "pass")
                        print(log.generate_log())
                        ml = MongoLogging.MongoLogging()
                        MongoLogging.MongoLogging.MongoLog(ml, request_number, "Prep.WeightScale",
                                                           grain[i] + "grain received.")
                    time.sleep(1)
                j = j + 1
                i = i + 1
            return weight_scale
        except Exception as e:
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"WeightScale\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(self.log_no + 1, "Prep.WeightScale", "Failed to dispense " + grain[i] + ".",
                      datetime.datetime.now(),
                      "fail")
            print(log.generate_log())
            ml = MongoLogging.MongoLogging()
            MongoLogging.MongoLogging.MongoLog(ml, request_number, "Prep.WeightScale",
                                               "Failed to dispense " + grain[i] + ".")
            print(e)

    # noinspection PyUnusedLocal,PyUnusedLocal,PyUnboundLocalVariable
    def read_weight_hops(self, recipe, request_number):
        '''
       Method that displays the actual weight of the hops
       Returns: Float of the weight goes into the weight scale with logging to ServiceNOW
        '''
        try:
            hop = list(recipe.hop_hop_amt.keys())
            weight = list(recipe.hop_hop_amt.values())
            weight = list(map(lambda x: float(x.replace(",", "")), weight))
            j = 1
            for i in range(len(hop)):
                weight_scale = 0.0
                status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"WeightScale\"}"
                sn_log = ServiceNowLog()
                ServiceNowLog.create_new_log(sn_log, status_log)
                log = Log(self.log_no + 1, "Prep.WeightScale", "Weight scale is set to zero.",
                          datetime.datetime.now(),
                          "pass")
                print(log.generate_log())
                ml = MongoLogging.MongoLogging()
                MongoLogging.MongoLogging.MongoLog(ml, request_number, "Prep.WeightScale",
                                                   "Weight scale is set to zero")
                time.sleep(1)
                status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"WeightScale\"}"
                sn_log = ServiceNowLog()
                ServiceNowLog.create_new_log(sn_log, status_log)
                log = Log(self.log_no + 1, "Prep.WeightScale", "Brewer is being asked to dispense " + hop[i] + ".",
                          datetime.datetime.now(),
                          "pass")
                print(log.generate_log())
                ml = MongoLogging.MongoLogging()
                MongoLogging.MongoLogging.MongoLog(ml, request_number, "Prep.WeightScale",
                                                   "Brewer is being asked to dispense " + hop[i] + ".")
                time.sleep(1)
                print(
                    "    \033[1m4." + str(j) + " To brew the beer for this batch, " + str(weight[i]) + " oz of " + hop[
                        i] + " Hops needed.\033[0m\n")
                time.sleep(1)
                print("       ****Weight scale is calibrated to \033[1m0.0\033[0m. \n")
                time.sleep(1)
                input("       Press Enter to dispense \033[1m" + hop[i] + "\033[0m Hops:\n")

                for weight_scale in arange(float(weight[i])):
                    weight_scale = weight_scale + 1
                    time.sleep(2)

                    print("       \033[1m" + str(weight_scale) + "\033[0m pound(s) \033[1m" + hop[
                        i] + "\033[0m Hops received. \033[1m" + str(
                        float(weight[i]) - weight_scale) + "\033[0m pound(s) left to be dispensed. \n")
                    time.sleep(1)
                    if float(weight[i]) == weight_scale:
                        time.sleep(1)
                        print("       \033[1m" + hop[i] + "\033[0m Hops are measured and \033[1m" + str(
                            weight_scale) + "\033[0m pounds received. \n")
                        time.sleep(1)
                        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"WeightScale\"}"
                        sn_log = ServiceNowLog()
                        ServiceNowLog.create_new_log(sn_log, status_log)
                        log = Log(self.log_no + 1, "Prep.WeightScale", hop[i] + " hop received.",
                                  datetime.datetime.now(),
                                  "pass")
                        print(log.generate_log())
                        ml = MongoLogging.MongoLogging()
                        MongoLogging.MongoLogging.MongoLog(ml, request_number, "Prep.WeightScale",
                                                           hop[i] + "hop received.")
                    time.sleep(2)
                j = j + 1
                i = i + 1
            return weight_scale
        except Exception as e:
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"WeightScale\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(self.log_no + 1, "Prep.WeightScale", "Failed to dispense " + hop[i] + ".",
                      datetime.datetime.now(),
                      "fail")
            print(log.generate_log())
            ml = MongoLogging.MongoLogging()
            MongoLogging.MongoLogging.MongoLog(ml, request_number, "Prep.WeightScale",
                                               "Failed to dispense " + hop[i] + ".")
            print(e)
