# Project: Brewing Automation System - Capstone Project
# Purpose Details: Thread and Prep I/O
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: 3/23
# Last Date Changed:4/7
# Rev

import RPi.GPIO as GPIO
from Sanitization import Sanitization
from Temperature import Temperature
import threading
import time
#from queue import Queue

# sensor = 11
pin = 4

# button for sanitization
s_button_pin = 26 # UP key
# button for temperature
t_button_pin = 13 # DOWN key

# Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(s_button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(t_button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

s = Sanitization(s_button_pin)
t = Temperature(t_button_pin)

# this function will called on staring of every thread
def thread_function(thread_id):
    try:
        s.button_function()
        try:
            tmp = t.read_temp()
            while( tmp > 80 or tmp < 60):
                print("\033[1;31;40m\t\b***Temperature of yeast is out of range.***\033[0;0m")
                print("\033[1;31;40m  ***Bring another yeast and measure temperature again.*** \033[0;0m\n")
                time.sleep(5)
                
                #print("      press down button to measure temperature of yeast: ")
                tmp = t.read_temp()
                # GPIO.wait_for_edge(t_button_pin, GPIO.FALLING)
            print("\033[1;32;40m       temperature of yeast is in range and ready to use.\033[0;0m\n")   
            time.sleep(2)
        except:
            
            GPIO.cleanup()
    except:
        
        GPIO.cleanup()

        

        
        
def main():
    time.sleep(2)
    thread_list = []
    # to create upto 5 Threads
    for x in range(5):
        message = ('\n Batch: '+ str(x+1) + ' ---------------------------------------')
        thread = threading.Thread(target=thread_function, args=(x,))
        thread_list.append(thread)
        # message = ('Batch: '+ str(x))
        print( message)
        

    # for thread in thread_list:
        thread.start()

    # for thread in thread_list:
        thread.join()
        #GPIO.cleanup()

if __name__ == '__main__':
	main()