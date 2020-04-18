# Project: Brewing Automation System - Capstone Project
# Purpose Details: Temperature Class - To get the temperature of Yeast
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/18
# Rev

# import RPi.GPIO as GPIO
import random
import time
from Brewing import ServiceNowLog

"""
# sensor = 11
pin = 4

# button for temperature
t_button_pin = 13 # DOWN key

# Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(t_button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
"""
class Temperature:
    """
    def __init__(self,button):
        self.button = button
    """

    def log(self):
        status_log = "{\"batch_id\":\"1\", \"brew_batch_stage\":\"Preparation\", \"log\":\"Starting Sanitation Process\"}"
        ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
        print(status_log)
    def read_temp(self):
        temperature = random.randrange(55, 85, 1)

        input("\033[1m    2. Press Enter to measure temperature of yeast: \033[0m")
        # GPIO.wait_for_edge(t_button_pin,GPIO.FALLING)
        time.sleep(3)
        # humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        # temperature = 9.0/5.0 * temperature + 32
        if temperature < 60 or temperature > 80:
            print('\t\t\tTemp = \033[1;31;40m{0:0.0f}*\033[0;0m F'.format(temperature))
        else:
            print('\t\t\tTemp = \033[1;32;40m{0:0.0f}*\033[0;0m F'.format(temperature))
        time.sleep(2)

        return temperature
        
    def yeast_temp(self):
        tmp = self.read_temp()
        while( tmp > 80 or tmp < 60):
            print("\033[1;31;40m\t\b***Temperature of yeast is out of range.***\033[0;0m")
            print("\033[1;31;40m  ***Bring another yeast and measure temperature again.*** \033[0;0m\n")
            time.sleep(5)
            
            #print("      press down button to measure temperature of yeast: ")
            tmp = self.read_temp()

            # GPIO.wait_for_edge(t_button_pin, GPIO.FALLING)
        print("\033[1;32;40m       Temperature of yeast is in range and ready to use.\033[0;0m\n")
        time.sleep(2)
        
         

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