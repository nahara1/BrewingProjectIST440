# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for connecting between cloud and local databases
# Course: IST 440W - 001
# Author: Erik Ellis (eae5206@psu.edu)
# Date Developed: 3/18/20
# Last Date Changed: 4/12/2020
# Rev 1

import logging, time


class DisplayHelper():

    def __init__(self):
        logging.info("Thread %s: starting DisplayHelper", self)  # Threading
        _lcd_display = object
        _led_matrix = object
        logging.info("Thread %s: finishing DisplayHelper", self)  # Threading

    logging.info("Thread %s: starting Getters and Setters")  # Threading

    def get_lcd_display_data(self):
        """
        Calls the LCD Display on the CrowPi
        :return: returns the LCD display
        """
        return self._lcd_display

    def set_lcd_display(self, display):
        """
        Sets the LCD display to display something
        :param display: LCD Display to be set
        :return: returns the display to be shown on the LCD of the CrowPi
        """
        self.lcd_display = display

    def print_start_info(self, stage_date_time, boil_time, boil_temp, is_boiling):
        """
        Prints start stage information to the screen
        :param stage_date_time: Start time of the stage
        :param boil_time: Time boil lasts
        :param boil_temp: Temperature
        :param is_boiling: Is it boiling
        """
        print("Start time: " + stage_date_time)
        print("Boil time (mins): " + boil_time)
        print("Boil temp: " + boil_temp)
        print("Is it boiling? : " + is_boiling)
        print('Now boiling for ' + boil_time)
        time.sleep(boil_time)
        print('Done boiling')
        Boil.update_boil_status(False)

    def print_end_info(self, end_stage_date_time, stage_duration):
        """
        Prints end stage information to the screen
        :param end_stage_date_time:  Time that the boil ends
        :param stage_duration:  Amount of time the stage lasted for
        """
        print("End time: " + end_stage_date_time)
        print("Boil stage duration (mins): " + stage_duration)
        print("Ending boil")

    def get_led_matrix_data(self):
        """
        Calls the LED Matrix on the CrowPi
        :return: returns the current LEDs on the LED Matrix
        """
        return self._led_matrix

    def set_led_matrix(self, matrix):
        """
        Sets the LED Matrix to turn LED lights off or on the matrix
        :param matrix: lights on the LED matrix
        :return: returns LEDs on the matrix
        """
        self._led_matrix = matrix

    logging.info("Thread %s: finishing Getters and Setters")  # Threading

    def send_data(self, display, matrix):
        """
        Sends Data to the matrix or display to change or turn on
        :param display: LCD display on the crowPi
        :param matrix: LED Matrix on the CrowPi
        :return: returns the display and metrix set up on the CrowPi
        """
        display, matrix
