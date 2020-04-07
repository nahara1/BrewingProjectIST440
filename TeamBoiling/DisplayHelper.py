# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Erik Ellis (eae5206@psu.edu)
# Date Developed: 3/18/20
# Last Date Changed:
# Rev 1

import logging

class DisplayHelper():

    def __init__(self):
        logging.info("Thread %s: starting DisplayHelper", self)  # Threading
        _lcd_display = object
        _led_matrix = object
        logging.info("Thread %s: finishing DisplayHelper", self)  # Threading

    logging.info("Thread %s: starting Getters and Setters")  # Threading

    def get_lcd_display_data(self):
        '''
        Calls the LCD Display on the CrowPi
        :return: returns the LCD display
        '''
        return self._lcd_display

    def set_lcd_display(self, display):
        '''
        Sets the LCD display to display something
        :param display: LCD Display to be set
        :return: returns the display to be shown on the LCD of the CrowPi
        '''
        self.lcd_display = display

    def get_led_matrix_data(self):
        '''
        Calls the LED Matrix on the CrowPi
        :return: returns the current LEDs on the LED Matrix
        '''
        return self._led_matrix

    def set_led_matrix(self, matrix):
        '''
        Sets the LED Matrix to turn LED lights off or on the matrix
        :param matrix: lights on the LED matrix
        :return: returns LEDs on the matrix
        '''
        self._led_matrix = matrix

    logging.info("Thread %s: finishing Getters and Setters")  # Threading

    def send_data(self, display, matrix):
        '''
        Sends Data to the matrix or display to change or turn on
        :param display: LCD display on the crowPi
        :param matrix: LED Matrix on the CrowPi
        :return: returns the display and metrix set up on the CrowPi
        '''
        display, matrix

