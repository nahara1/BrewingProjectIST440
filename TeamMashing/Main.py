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
from TeamMashing.SpargingTank import SpargingTank
#from HotLiquorTank import HotLiquorTank
from TeamMashing.Wort import Wort

def start_mashing_process(): # Mashing process start
    m = MillingMachine(1, 1) # setting an object to milling machine, machine id and time
    m.mill_grains() # execution to milled grains

    st = SpargingTank(2, 1, 1, 1, 1, 1, 1)
    st.stir()

    w = Wort(3, 1, 1, 1)
    w.separate_wort()

if __name__ == "__main__": # verify main method
    start_mashing_process()  # initiates mashing process
