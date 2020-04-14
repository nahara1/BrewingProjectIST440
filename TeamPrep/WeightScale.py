# Project: Brewing Automation System - Capstone Project
# Purpose Details: WeightScale Class
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/7
# Rev

import RPi.GPIO as GPIO
import random
import time
import numpy

# sensor = 11
# pin = 4

# button for weight
w_button_pin =  19# Right key

# Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(w_button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

class WeightScale:
    def __init__(self,button):
        self.button = button

    def read_weight_grains(self):
        weight_scale = 0.0
        weight = random.randrange(2,5, 1)*1.0
        print("    3. To brew the beer for this batch, \033[1;34;40m" + str(weight) + "\033[0;0m pounds of All Grains needed.")
        print("       ****Weight scale is calibrated to \033[1;34;40m0.0\033[0;0m. \n")
        print("       To dispense \033[1;33;40m1\033[0;0m packet of \033[1;33;40m1.0\033[0;0m pound All Grain each time on weight scale hit the enter : \n")
        print("       Hit the right button to dispense one All Grain packet:")
        for weight_scale in numpy.arange(0, weight):
            weight_scale = weight_scale + 1
            GPIO.wait_for_edge(w_button_pin, GPIO.FALLING)
            time.sleep(2)
           # print("     Press right button to dispense 1 packet of 1 pound All Grains on weight scale : ")
           # time.sleep(2)
            print("       \033[1;31;40m" + str(weight_scale) + "\033[0;0m pound(s) All Grains recieved. \033[1;33;40m" + str(weight-weight_scale) + "\033[0;0m pound(s) left to be dispensed. \n")
            if weight==weight_scale:
                print("      \033[1;32;40m All Grains are measured and " + str(weight_scale) + " pounds recieved. \033[0;0m \n")
            else:
                #print("       \033[1;31;40m" + str(weight_scale) + "\033[0;0m pound(s) All Grains recieved. \033[1;33;40m" + str(weight-weight_scale) + "\033[0;0m pound(s) left to be dispensed. \n")
                print("       Hit the right button to dispense one more packet: ")
            time.sleep(2)
        return weight_scale
    

    def read_weight_hops(self):
        weight_scale = 0.0
        weight = random.randrange(1,5, 1)*0.5
        print("    4. To brew the beer for this batch, \033[1;34;40m" + str(weight) + "\033[0;0m pounds of Hops needed.")
        print("       ****Weight scale is calibrated to \033[1;34;40m0.0\033[0;0m. \n")
        print("       To dispense \033[1;33;40m1\033[0;0m packet of \033[1;33;40m0.5\033[0;0m pound Hops each time on weight scale hit the enter : \n")
        print("       Hit the right button to dispense one packet of Hops:")
        for weight_scale in numpy.arange (0, weight):
            weight_scale = weight_scale + 0.5
            GPIO.wait_for_edge(w_button_pin, GPIO.FALLING)
            time.sleep(2)
           # print("     Press right button to dispense 1 packet of 1 pound Hops on weight scale : ")
           # time.sleep(2)
            print("       \033[1;31;40m" + str(weight_scale) + "\033[0;0m pound(s) Hops recieved. \033[1;33;40m" + str(weight-weight_scale) + "\033[0;0m pound(s) left to be dispensed. \n")
            if weight==weight_scale:
                print("      \033[1;32;40m Hops are measured and " + str(weight_scale) + " pounds recieved. \033[0;0m \n")
            else:
                #print("       \033[1;31;40m" + str(weight_scale) + "\033[0;0m pound(s) Hops recieved. \033[1;33;40m" + str(weight-weight_scale) + "\033[0;0m pound(s) left to be dispensed. \n")
                print("       Hit the right button to dispense one more packet: ")
            time.sleep(2)
        return weight_scale
  """      
    def read_weight_sugar(self):
        weight_scale = 0.0
        weight = random.randrange(1,4, 1)*0.05
        print("    4. To brew the beer for this batch, \033[1;34;40m" + str(weight) + "\033[0;0m pounds of Sugar needed.")
        print("       ****Weight scale is calibrated to \033[1;34;40m0.0\033[0;0m. \n")
        print("       To dispense \033[1;33;40m1\033[0;0m packet of \033[1;33;40m0.05\033[0;0m pound Sugar each time on weight scale hit the enter : \n")
        print("       Hit the right button to dispense one packet of sugar:")
        for weight_scale in numpy.arange (0, weight):
            weight_scale = weight_scale + 0.05
            GPIO.wait_for_edge(w_button_pin, GPIO.FALLING)
            time.sleep(2)
           # print("     Press right button to dispense 1 packet of 0.05 pound sugar on weight scale : ")
           # time.sleep(2)
            print("       \033[1;31;40m" + str(weight_scale) + "\033[0;0m pound(s) Sugar recieved. \033[1;33;40m" + str(weight-weight_scale) + "\033[0;0m pound(s) left to be dispensed. \n")
            if weight==weight_scale:
                print("      \033[1;32;40m Sugsr are measured and " + str(weight_scale) + " pounds recieved. \033[0;0m \n")
            else:
                #print("       \033[1;31;40m" + str(weight_scale) + "\033[0;0m pound(s) Sugar recieved. \033[1;33;40m" + str(weight-weight_scale) + "\033[0;0m pound(s) left to be dispensed. \n")
                print("       Hit the right button to dispense one more packet: ")
            time.sleep(2)
        return weight_scale
        
  """  
