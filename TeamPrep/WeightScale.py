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
from TeamPrep.Temperature import Temperature

t = Temperature()
# noinspection PyUnusedLocal,PyMethodMayBeStatic,PyMethodMayBeStatic,PyMethodMayBeStatic
class WeightScale:

    def __init__(self):  # constructor initialized field

        self.log_no = t.log_no
        self.hop_hop_amt = None
        self.grain = None

    # noinspection PyArgumentList,PyArgumentList
    def get_grain(self):
        self.grain = Recipe.Recipe.get_grain()
        return self.grain

    # noinspection PyArgumentList,PyArgumentList
    def get_hop_hop_amt(self):
        self.hop_hop_amt = Recipe.Recipe.get_hop_hop_amt()
        return self.hop_hop_amt

    '''
    interface for weighing grains
    '''

    # noinspection PyUnboundLocalVariable
    def read_weight_grains(self, recipe, request_number):
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
            time.sleep(1)
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"WeightScale\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(self.log_no + 1, "Prep.WeightScale", "Hops list and weight copied from ordered brew recipe.",
                      datetime.datetime.now(),
                      "pass")
            print(log.generate_log())
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
                time.sleep(1)
                status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"WeightScale\"}"
                sn_log = ServiceNowLog()
                ServiceNowLog.create_new_log(sn_log, status_log)
                log = Log(self.log_no + 1, "Prep.WeightScale", "Brewer is being asked to dispense " + grain[i] + ".",
                          datetime.datetime.now(),
                          "pass")
                print(log.generate_log())
                time.sleep(1)
                print("    \033[1m3." + str(j) + " To brew the beer for this batch, " + str(weight[i]) + " pounds of " +
                      grain[i]
                      , " needed.\033[0m\n"
                      )
                time.sleep(2)
                print("       ****Weight scale is calibrated to \033[1m0.0\033[0m. \n")
                time.sleep(1)
                input("       Press the Enter to dispense \033[1m" + grain[i] + "\033[0m:\n")

                for weight_scale in arange(float(weight[i])):
                    weight_scale = weight_scale + 1.0
                    time.sleep(2)
                    print("       \033[1m" + str(
                        weight_scale) + "\033[0;0m pound(s) \033[1m" + grain[i] + "\033[0m received. \033[1m" + str(
                        weight[i] - weight_scale) + "\033[0m pound(s) left to be dispensed. \n")
                    time.sleep(2)
                    if float(weight[i]) == weight_scale:
                        print("       \033[1m" + grain[i] + "\033[0m are measured and \033[1m" + str(
                            weight_scale) + "\033[0m pounds received.  \n")
                        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"WeightScale\"}"
                        sn_log = ServiceNowLog()
                        ServiceNowLog.create_new_log(sn_log, status_log)
                        log = Log(t.log_no + 1, "Prep.WeightScale", grain[i] + " grain received.",
                                  datetime.datetime.now(),
                                  "pass")
                        print(log.generate_log())
                    time.sleep(2)
                j = j + 1
                i = i + 1
            return weight_scale
        except Exception as e:
            status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"WeightScale\"}"
            sn_log = ServiceNowLog()
            ServiceNowLog.create_new_log(sn_log, status_log)
            log = Log(self.log_no + 1, "Prep.WeightScale", "Failed to dispense " + grain[i] +".",
                      datetime.datetime.now(),
                      "fail")
            print(log.generate_log())
            print(e)

    '''
    logging of weight measurements
    '''
    '''
    interface for weighing hops
    '''

    # noinspection PyUnusedLocal,PyUnusedLocal,PyUnboundLocalVariable
    def read_weight_hops(self, recipe, request_number):
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
                time.sleep(1)
                status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"WeightScale\"}"
                sn_log = ServiceNowLog()
                ServiceNowLog.create_new_log(sn_log, status_log)
                log = Log(self.log_no + 1, "Prep.WeightScale", "Brewer is being asked to dispense " + hop[i] + ".",
                          datetime.datetime.now(),
                          "pass")
                print(log.generate_log())
                time.sleep(1)
                print(
                    "    \033[1m4." + str(j) + " To brew the beer for this batch, " + str(weight[i]) + " oz of " + hop[
                        i] + " Hops needed.\033[0m\n")
                time.sleep(2)
                print("       ****Weight scale is calibrated to \033[1m0.0\033[0m. \n")
                time.sleep(2)
                print("       To dispense \033[1m1\033[0m packet of \033[1m1.0\033[0m oz \033[1m" + hop[
                    i] + "\033[0m Hops : \n")
                time.sleep(2)
                input("       Press Enter button to dispense one packet of \033[1m" + hop[i] + "\033[0m Hops:\n")

                for weight_scale in arange(float(weight[i])):
                    weight_scale = weight_scale + 1
                    time.sleep(2)

                    print("       \033[1m" + str(weight_scale) + "\033[0m pound(s) \033[1m" + hop[
                        i] + "\033[0m Hops received. \033[1m" + str(
                        float(weight[i]) - weight_scale) + "\033[0m pound(s) left to be dispensed. \n")
                    time.sleep(2)
                    if float(weight[i]) == weight_scale:
                        time.sleep(2)
                        print("       \033[1m" + hop[i] + "\033[0m Hops are measured and \033[1m" + str(
                            weight_scale) + "\033[0m pounds received. \n")
                        time.sleep(2)
                        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Prep\", \"log\":\"WeightScale\"}"
                        sn_log = ServiceNowLog()
                        ServiceNowLog.create_new_log(sn_log, status_log)
                        log = Log(self.log_no + 1, "Prep.WeightScale", hop[i] + " grain received.",
                                  datetime.datetime.now(),
                                  "pass")
                        print(log.generate_log())
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
            print(e)
