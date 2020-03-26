# Project: Brewing Automation System - Capstone Project
# Purpose Details: class for controlling sensors
# Course: IST 440W - 001
# Author: Teresa Barker(tlb5767@psu.edu)
# Date Developed: 3/18/20
# Last Date Changed: 3/18/2020
# Rev 1


class SensorHelper:

    # Variables
    _touch_sensor = bool
    _buzzer_status = bool
    _sensor_values = float

    def __init__(self, _touch_sensor, _buzzer_status, _sensor_values):
        self._touch_sensor = _touch_sensor
        self._buzzer_status = _buzzer_status
        self._sensor_values = _sensor_values

    # Getters and Setters
    # Sensor Values
    def get_sensor_values(self):
        return self._sensor_values

    def set_sensor_values(self, _sensor_values):
        self._sensor_values = _sensor_values

    # Buzzer Status
    def get_buzzer_status(self):
        return self._buzzer_status

    def set_buzzer_status(self, _buzzer_status):
        self._buzzer_status = _buzzer_status

    # Touch Sensor
    def get_touch_sensor(self):
        return self._touch_sensor

    def set_touch_sensor(self, _touch_sensor):
        self._touch_sensor = _touch_sensor

    # Methods
    def send_values(self):
        return self.send_values()


