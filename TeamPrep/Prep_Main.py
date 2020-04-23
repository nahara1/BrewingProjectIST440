# Project: Brewing Automation System - Capstone Project
# Purpose Details: Thread and Prep I/O
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/18
# Rev

import threading
import time

from TeamPrep import QualityCheck_Prep
from TeamPrep.Sanitization import Sanitization
from TeamPrep.Temperature import Temperature
from TeamPrep.WeightScale import WeightScale
from Brewing.ServiceNowLog import ServiceNowLog

s = Sanitization()
t = Temperature()
w = WeightScale()
s1 = ServiceNowLog()
# this function will called on staring of every thread



def thread_function():
    '''
    Method thread function will gather each of Team Preps functionality
    return: Threading into the main method below with exceptions
    '''
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
    '''
    Main Method for Team Prep to excute
    return: excutes main method with threads
    '''
    time.sleep(2)
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