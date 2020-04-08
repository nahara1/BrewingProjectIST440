# Project: Brewing Project
# Purpose Details: Main control unit for mashing
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 3/18/2020
# Rev: 1.1

from TeamMashing.MillingMachine import MillingMachine
from TeamMashing.HotLiquorTank import HotLiquorTank
import threading

def start_mashing_process(): # Mashing process start

    """
    Mashing Process Executes
    :returns: void
    """

    m = MillingMachine(1, 10) # setting an object to milling machine, machine id and time

    t1 = threading.Thread(target=m.mill_grains)

    hlt = HotLiquorTank(2, 1, 1)

    t2 = threading.Thread(target=hlt.send_hot_water_to_sparging_tank())

    t1.start()
    t2.start()

if __name__ == "__main__": # verify main method
    start_mashing_process()  # initiates mashing process
