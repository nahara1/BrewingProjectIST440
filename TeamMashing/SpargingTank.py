# Project: Brewing Project
# Purpose Details: Sparging tank transfer and automation
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 3/24/2020
# Rev: 1.2
class SpargingTank: #constructor for class sparging tank
    def __init__(self, Sid,stirr_time,water_temp,water_amt,heat_time, sparg_time, milled_amount,):
        self.machine_id = Sid
        self.stirring_time = stirr_time
        self.heating_time = heat_time
        self.water_amount = water_amt
        self.water_temp = water_temp
        self.sparging_time = sparg_time
        self.milled_grain_amount = milled_amount

    def add_milled_grains(self):
        #adding grains to the tank
        return "Milled Gains added to tank"
    def add_water(self):
        #adding heated water to tank
        return "Water pumped into tank"
    def stirr(self):
        #stirring the wort in progress
        return "Stirring up the sparging tank"
    def heat(self):
        #heat the tank for a defined time while stirring.
        return "Proper tempature acheved"
    def sparg_the_tank(self):
        #empty the tank while spraying water over the remaing grains.
        return "Tank emptying, washing grains."