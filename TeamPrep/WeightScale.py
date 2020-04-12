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

    def read_weight(self):
        weight_scale = 0
        weight = random.randrange(2,4, 1)
        print("    3. To brew the beer for this batch, \033[1;34;40m" + str(weight) + "\033[0;0m pounds of All Grains needed.")
        print("       ****Weight scale is calibrated to \033[1;34;40m0\033[0;0m. \n")
        print("       To dispense \033[1;33;40m1\033[0;0m packet of \033[1;33;40m1\033[0;0m pound All Grain each time on weight scale hit the enter : \n")
        print("       Hit the right button to dispense one All Grain packet:")
        for weight_scale in range (0, weight):
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
        
    

# # USAGE
# t = temperature(t_button_pin)
# try:
#     tmp = t.read_temp()
#     while( tmp > 70 or tmp < 60):
#         tmp = t.read_temp()
#     print("temperature is in range.")
# except:
#     GPIO.cleanup()
# GPIO.cleanup()