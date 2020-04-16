# Project: Brewing Automation System - Capstone Project
# Purpose Details: Kegging - Keg Class
# Course: IST 440W - 001
# Author: Ronald Salguero
# Date Developed: 4/4/2020
# Last Date Changed:
# Rev: 1.0

class Keg:
    def __init__(self, keg_id, current_volume, max_volume, keg_pressure, kegstyle):
        self.keg_id = keg_id
        self.current_volume = current_volume
        self.max_volume = max_volume
        self.keg_pressure = keg_pressure
        self.keg_style = kegstyle