# Project: Brewing Automation System - Capstone Project
# Purpose Details: Thread and Prep I/O
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/18
# Rev

# import RPi.GPIO as GPIO
from TeamPrep import QualityCheck_Prep
from TeamPrep.Sanitization import Sanitization
from TeamPrep.Temperature import Temperature
from TeamPrep.WeightScale import WeightScale
from Brewing import ServiceNowLog
import threading
import time

# from queue import Queue
"""
# sensor = 11
pin = 4

# button for sanitization
s_button_pin = 26 # UP key
# button for temperature
t_button_pin = 13 # DOWN key
# button for weight
w_button_pin = 19 # Right key

# Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(s_button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(t_button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(w_button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
"""
s = Sanitization()
t = Temperature()
w = WeightScale()
# b = BrewRequest()
# q = QualityCheck_Prep()


# this function will called on staring of every thread
'''
This thread function will be called each time this file runs to check them temperature of the yeast to see if the yeast is ready for use
'''


def thread_function(thread_id):
    while True:
        try:
            print()
            # s.sanitization()
            try:
                print()
                # t.yeast_temp()
                try:
                    w.read_weight_grains()
                    try:
                        w.read_weight_hops()
                        try:
                            w.read_weight_sugar()
                            try:
                                QualityCheck_Prep.QualityCheck.get_QA_Check()
                            except:
                                break
                        except:
                            # GPIO.cleanup()
                            break
                    except:
                        # GPIO.cleanup()
                        break
                except:
                    # GPIO.cleanup()
                    break
            except:
                # GPIO.cleanup()
                break
        except:
            # GPIO.cleanup()
            break
        break


def prep_main():
    time.sleep(2)
    thread_list = []
    # to create upto 5 Threads
    for x in range(5):
        # status_log = "{\"batch_id\":\"1\", \"brew_batch_stage\":\"Preparation\", \"log\":\"Starting Preparation Process\"}"
        # ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
        message = ('\n\n Batch: ' + str(x + 1) + ' ---------------------------------------')
        thread = threading.Thread(target=thread_function, args=(x,))
        thread_list.append(thread)
        # message = ('Batch: '+ str(x))
        print(message)
        '''
       This is the main method
        '''

        # for thread in thread_list:
        thread.start()

        # for thread in thread_list:
        thread.join()
        # GPIO.cleanup()


if __name__ == '__main__':
    prep_main()
