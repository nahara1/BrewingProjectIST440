# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for controlling sensors
# Course: IST 440W - 001
# Author: Teresa Barker (tlb5767@psu.edu), Alex Hirsh (ajh6196@psu.edu)
# Date Developed: 3/18/20
# Last Date Changed: 4/14/2020
# Rev 4

import logging


class SensorHelper:

    # Variables
    _touch_sensor = bool
    _buzzer_status = bool
    _sensor_values = float

    def __init__(self, _touch_sensor, _buzzer_status, _sensor_values):
        """
        Constructor method sensor variables to be accessed
        :param _touch_sensor: touch sensor on the crowPi
        :param _buzzer_status: status of the buzzer on the CrowPi
        :param _sensor_values: values for the sensor
        """
        logging.info("Thread %s: starting SensorHelper", self)
        self._touch_sensor = _touch_sensor
        self._buzzer_status = _buzzer_status
        self._sensor_values = _sensor_values
        logging.info("Thread %s: finishing SensorHelper", self)

    # Getters and Setters
    # Sensor Values
    logging.info("Thread %s: starting Getters and Setters")

    def get_sensor_values(self):
        """
        Calls the values of the sensor
        :return: returns the values of the sensor
        """
        return self._sensor_values

    def set_sensor_values(self, _sensor_values):
        """
        Setter for the values of the sensor
        :param _sensor_values: sensor values that were called
        :return: returns and sets the sensor values
        """
        self._sensor_values = _sensor_values

    # Buzzer Status
    def get_buzzer_status(self):
        """
        Calls the buzzer to retrieve the status
        :return: returns the buzzer's status
        """
        return self._buzzer_status

    def set_buzzer_status(self, _buzzer_status):
        """
        Setter for the buzzer status
        :param _buzzer_status: status of the buzzer that's called
        :return: returns the status and sets it for the buzzer
        """
        self._buzzer_status = _buzzer_status

    # Touch Sensor
    def get_touch_sensor(self):
        """
        Calls the Touch sensor
        :return: returns the touch sensor
        """
        return self._touch_sensor

    def set_touch_sensor(self, _touch_sensor):
        """
        Setter for the touch sensor
        :param _touch_sensor: touch sensor's status
        :return: returns the touch sensor and sets it to see if it's being touched or not
        """
        self._touch_sensor = _touch_sensor

    logging.info("Thread %s: finishing Getters and Setters")

    # Methods
    def send_values(self):
        """
        Sends values to the sensors to access and utilize them
        :return: returns values sent to the sensors
        """
        logging.info("Thread %s: starting Send_Values", self)
        return self.send_values()
        logging.info("Thread %s: finishing Send_Values", self)





    def get_buzzer(self):
        print("Buzzzzz, Timer is done.")



