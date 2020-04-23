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

s = Sanitization()
t = Temperature()
w = WeightScale()

# this function will called on staring of every thread
'''
This thread function will be called each time this file runs to check them temperature of the yeast to see if the yeast is ready for use
'''


def thread_function():
    while True:
        try:
            s.sanitization(s)
            try:
                t.yeast_temp(t)
                try:
                    w.read_weight_grains(w)
                    try:
                        w.read_weight_hops(w)
                        try:
                            QualityCheck_Prep.QualityCheck.get_QA_Check()
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
