# Project: Brewing Project
# Purpose Details: Brite Tank Object
# Course: IST 440W
# Author: Team Kegging - Daibo Zhang
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
               "Brite_Max_Volume: {}\n" \
               "Brite_Volume: {}\n" \
               "Brite_Pressure: {}\n" \
               "Brite_Beer: {}\n".format(self.bt_id, self.tank_temp, self.tank_max_volume, self.tank_current_volume, self.tank_pressure, self.beer_type)

    def get_carbonation(self):
        temp30f = [0,1.82,1.92,2.03,2.14,2.23,2.36,2.48,2.6,2.7,2.82,2.93,3.02,3.13,3.24,3.35,3.46,3.57,3.67,3.78,3.89,4,4.11,4.22,4.33,4.44,4.66,4.77,4.87,4.98,4.98]
        temp31f
        temp32f
        temp33f
        temp34f
        temp35f
        temp36f
        temp37f
        temp38f
        temp39f
        temp40f
        temp41f
        temp42f
        temp43f
        temp33f
        temp44f
        temp45f
        temp46f
        temp47f
        temp48f
        temp49f
        temp50f
        temp51f
        temp52f
        temp53f
        temp54f
        temp55f
        temp56f
        temp57f
        temp58f
        temp59f
        temp60f
        temp61f
        temp62f
        temp63f
        temp64f
        temp65f

tk = KeggingBriteTank(311,79,5.22,2.01,32,"Ale")

print(tk.get_status())
tk.get_carbonation()