# Project: Brewing Project
# Purpose Details: Main control unit for mashing
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 3/18/2020
# Rev: 1.1

import sys
import time

from Log import Log
from TeamMashing.MillingMachine import MillingMachine
#from SpargingTank import SpargingTank
#from HotLiquorTank import HotLiquorTank

def start_mashing_process():
    m = MillingMachine(1, 1)
    m.mill_grains()

if __name__ == "__main__":
    start_mashing_process()
