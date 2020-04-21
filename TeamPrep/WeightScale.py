# Project: Brewing Automation System - Capstone Project
# Purpose Details: WeightScale Class - To weigh grains, hops and sugar
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/18
# Rev 1

# import RPi.GPIO as GPIO
import random
import time
from numpy import arange
import copy
from Brewing.Recipe import Recipe
from Brewing.ServiceNowLog import ServiceNowLog
from Brewing.BrewRequest import Recipe


# sensor = 11
# pin = 4

# button for weight
# w_button_pin =  19# Right key

# Pin setup
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(w_button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

class WeightScale:
    # def __init__(self,button):
    #    '''
    #   Defines attributes of sanitization
    #   '''
    #    self.button = button
    #   '''
    #  Adds method to the attribute for sanitization
    #    '''

    def __init__(self):  # constructor initalized field

        self.hop_hop_amt = None
        self.grain = None

    def get_grain(self):
        self.grain = Recipe.Recipe.get_grain()
        return self.grain

    def get_hop_hop_amt(self):
        self.hop_hop_amt = Recipe.Recipe.get_hop_hop_amt()
        return self.hop_hop_amt

    '''
    interface for weighing grains
    '''

    def read_weight_grains(self, recipe):

        global weight_scale
        grain = list(recipe.grain.keys())
        weight = list(recipe.grain.values())
        weight = list(map(lambda x: float(x.replace(",", "")), weight))

        j = 1
        for i in range(len(grain)):
            weight_scale = 0.0

            print("    \033[1m3." + str(j) + " To brew the beer for this batch, " + str(weight[i]) + " pounds of " + grain[i]
                  , " needed.\033[0m\n"
                  )
            time.sleep(2)
            print("       ****Weight scale is calibrated to \033[1m0.0\033[0m. \n")
            time.sleep(1)
            print("       To dispense \033[1m1\033[0m packet of \033[1m1.0\033[0m pound \033[1m" + grain[i] + "\033[0m : \n")
            time.sleep(1)
            input("       Press the right button to dispense one \033[1m" + grain[i] + "\033[0m packet:\n")


            for weight_scale in arange(float(weight[i])):
                weight_scale = weight_scale + 1.0
                # GPIO.wait_for_edge(w_button_pin, GPIO.FALLING)
                time.sleep(2)
                # print("     Press Enter to dispense 1 packet of 1 pound All Grains on weight scale : ")
                # time.sleep(2)
                print("       \033[1m" + str(
                    weight_scale) + "\033[0;0m pound(s) \033[1m" + grain[i] + "\033[0m received. \033[1m" + str(
                    weight[i] - weight_scale) + "\033[0m pound(s) left to be dispensed. \n")
                if float(weight[i]) == weight_scale:
                    print("       \033[1m" + grain[i] + "\033[0m are measured and \033[1m" + str(
                        weight_scale) + "\033[0m pounds received.  \n")
                else:
                    # print("       \033[1;31;40m" + str(weight_scale) + "\033[0;0m pound(s) All Grains recieved. \033[1;33;40m" + str(weight-weight_scale) + "\033[0;0m pound(s) left to be dispensed. \n")
                    input("       Press the right button to dispense one more packet of \033[1m" + grain[i] + "\033[0m: ")
                time.sleep(2)
            j = j + 1
            i = i + 1

        return weight_scale

    '''
    logging of weight measurments
    '''
    '''
    interface for weighing hops
    '''

    def read_weight_hops(self, recipe):

        global weight_scale

        hop = list(recipe.hop_hop_amt.keys())
        weight = list(recipe.hop_hop_amt.values())
        weight = list(map(lambda x: float(x.replace(",", "")), weight))
        j = 1
        for i in range(len(hop)):
            weight_scale = 0.0
            print("    \033[1m4." + str(j) + " To brew the beer for this batch, " + str(weight[i]) + " oz of " + hop[i] + " Hops needed.\033[0m\n")
            time.sleep(2)
            print("       ****Weight scale is calibrated to \033[1m0.0\033[0m. \n")
            time.sleep(2)
            print("       To dispense \033[1m1\033[0m packet of \033[1m1.0\033[0m oz \033[1m" + hop[i] + "\033[0m Hops : \n")
            time.sleep(2)
            input("       Press Enter button to dispense one packet of \033[1m" + hop[i] + "\033[0m Hops:\n")

            for weight_scale in arange(float(weight[i])):
                weight_scale = weight_scale + 1
                # GPIO.wait_for_edge(w_button_pin, GPIO.FALLING)
                time.sleep(2)
                # print("     Press right button to dispense 1 packet of 0.5 pound Hops on weight scale : ")
                # time.sleep(2)

                print("       \033[1m" + str(weight_scale) + "\033[0m pound(s) \033[1m" + hop[i] + "\033[0m Hops recieved. \033[1m" + str(
                    float(weight[i]) - weight_scale) + "\033[0m pound(s) left to be dispensed. \n")
                if float(weight[i]) == weight_scale:
                    time.sleep(2)
                    print("       \033[1m" + hop[i] + "\033[0m Hops are measured and \033[1m" + str(weight_scale) + "\033[0m pounds recieved. \n")
                else:
                    # print("       \033[1;31;40m" + str(weight_scale) + "\033[0;0m pound(s) Hops recieved. \033[1;33;40m" + str(weight-weight_scale) + "\033[0;0m pound(s) left to be dispensed. \n")
                    time.sleep(2)
                    input("       Press the right button to dispense one more packet \033[1m" + hop[i] + "\033[0m: \n")
                time.sleep(2)
            j = j + 1
            i = i + 1
        return weight_scale

    '''
    interface for weighing sugar
    '''

    def read_weight_sugar(self):
        weight_scale = 0.00
        weight = random.randrange(0, 4, 1) * 0.05
        time.sleep(2)
        print("    \033[1m5. To brew the beer for this batch, " + str(weight) + " pounds of Sugar needed.\033[0m\n")
        time.sleep(2)
        if weight == 0.0:
            print("       No Sugar needed to brew this batch order. \n")
        else:
            print("       ****Weight scale is calibrated to \033[1m0.0\033[0m. \n")
            time.sleep(1)
            print("       To dispense \033[1m1\033[0m packet of \033[1m0.05\033[0m pound Sugar : \n")
            time.sleep(1)
            input("       Press Enter to dispense one packet of sugar:\n")
            for weight_scale in arange(0.00, weight + 0.01, 0.05):
                if weight_scale > 0:
                    # GPIO.wait_for_edge(w_button_pin, GPIO.FALLING)
                    time.sleep(2)
                    # print("     Press right button to dispense 1 packet of 0.05 pound sugar on weight scale : ")
                    # time.sleep(2)
                    print("       \033[1m" + str(
                        weight_scale) + "\033[0m pound(s) Sugar received. \033[1m" + str(
                        weight - weight_scale) + "\033[0m pound(s) left to be dispensed. \n")
                    if weight == weight_scale:
                        time.sleep(2)
                        print("       Sugar are measured and \033[1m" + str(
                            weight_scale) + "\033[0m pounds received. \n")
                        time.sleep(2)
                    else:
                        # print("       \033[1;31;40m" + str(weight_scale) + "\033[0;0m pound(s) Sugar recieved. \033[1;33;40m" + str(weight-weight_scale) + "\033[0;0m pound(s) left to be dispensed. \n")
                        time.sleep(2)
                        input("       Press Enter to dispense one more packet: ")
                    time.sleep(2)
        return weight_scale

