# Project: Brewing Project
# Purpose Details: Main control for Kegging
# Course: IST 440W
# Author: Team Kegging
# Date Developed: 4/14/2020
# Last Date Changed: 4/14/2020
# Rev: 1.0

from TeamKegging.KeggingBriteTank import KeggingBriteTank

testtank = KeggingBriteTank(1,35.78987,5.00,3.43,21,"Ale")
testtank.update_tank_temp(37)
print(testtank.get_carbonation())