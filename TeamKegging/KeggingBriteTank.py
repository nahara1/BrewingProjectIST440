# Project: Brewing Project
# Purpose Details: Brite Tank Object
# Course: IST 440W
# Author: Team Kegging
# Date Developed: 4/03/2020
# Last Date Changed: 4/03/2020
# Rev: 1.0

import datetime
from Log import Log

class KeggingBriteTank:  #Brite Tank
    def __init__(self, bt_id, tank_temp, tank_max_volume, tank_current_volume, tank_pressure, beer_type):
        self.bt_id = bt_id
        self.tank_temp = tank_temp
        self.tank_max_volume = tank_max_volume
        self.tank_current_volume = tank_current_volume
        self.tank_pressure = tank_pressure
        self.beer_type = beer_type

    def get_status(self):
        return "Brite_ID: {}\n" \
               "Brite_Temp: {}\n" \
               "Brite_Volume: {}\n" \
               "Brite_Pressure: {}\n" \
               "Brite_Beer: {}\n".format(self.bt_id, self.tank_temp, self.tank_current_volume, self.tank_pressure, self.beer_type)


tk = KeggingBriteTank(311,79,5.22,2.01,32,"Ale")

print(tk.get_status())