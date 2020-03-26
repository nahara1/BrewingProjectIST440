# Project: Brewing Project
# Purpose Details: Automate Hot Liquor Tank Process
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 3/24/2020
# Rev: 1.1

class HotLiquorTank:
    def __init__(self, tID, wVolume, wtemperature):
        self.tank_ID = tID
        self.water_amount = wVolume
        self.water_temp = wtemperature
        self.is_transferred = False

    def get_tank_ID(self):
        return self.tID

    def get_water(self):
        return self.wVolume

    def send_hot_water(self):
        return ("Hot water is sent.")

    def check_water_temp(self):
        return self.wtemperature