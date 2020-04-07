# Project: Brewing Automation System - Capstone Project
# Purpose Details: Employee Class
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/5
# Rev

import RPi.GPIO as GPIO

# sensor = 11
pin = 4

# button for temperature
t_button_pin = 13 # DOWN key

# Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(t_button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

class temperature:
    def __init__(self,button):
        self.button = button

    def read_temp(self):
        temperature = random.randrange(55, 85, 1)
        print("press down button to measure temperature.")
        GPIO.wait_for_edge(t_button_pin,GPIO.FALLING)
        # humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        # temperature = 9.0/5.0 * temperature + 32
        print('Temp={0:0.0f}* F'.format(temperature))
        return temperature

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