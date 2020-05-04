# Project: Brewing Automation System - Capstone Project
# Purpose Details: Thread and Prep I/O
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/18
# Rev

import threading
import time
import sys

from TeamPrep import QualityCheck_Prep
from TeamPrep.Sanitization import Sanitization
from TeamPrep.Temperature import Temperature
from TeamPrep.WeightScale import WeightScale
from Brewing.ServiceNowLog import ServiceNowLog

s = Sanitization()
t = Temperature()
w = WeightScale()
s1 = ServiceNowLog()
# this function will be called on the start of every thread
sleep_time = .25


def thread_function():
    """
    Method thread function that gathers each of Prep's functionality
    Threading is implemented in the main method below with exception handling
    :return: void
    """
    while True:
        try:
            s.sanitization()
            try:
                t.yeast_temp()
                try:
                    w.read_weight_grains()
                    try:
                        w.read_weight_hops()
                        try:
                            QualityCheck_Prep.QualityCheck.get_QA_Check(request_number)
                        except Exception as e:
                            print(e)
                    except Exception as e:
                        print(e)
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
        break


# noinspection SpellCheckingInspection
def prep_main():
    """
    Main Method Call for Team Prep to excute and implement threading
    :return:
    """
    time.sleep(sleep_time * 2)
    thread_list = []
    # to create up to 5 Threads
    for x in range(5):
        # status_log = "{\"batch_id\":\"1\", \"brew_batch_stage\":\"Preparation\", \"log\":\"Starting Preparation Process\"}"
        # ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
        message = ('\n\n Batch: ' + str(x + 1) + ' ---------------------------------------')
        thread = threading.Thread(target=thread_function, args=(x,))
        thread_list.append(thread)
        # message = ('Batch: '+ str(x))
        print(message)

        # for thread in thread_list:
        thread.start()

        # for thread in thread_list:
        thread.join()
        # GPIO.cleanup()


if __name__ == '__main__':
    prep_main()
