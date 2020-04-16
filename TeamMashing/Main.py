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

    m = MillingMachine() # setting an object to milling machine, machine id and time

    t1 = threading.Thread(target=m.check_grains_weight())

    t1.start()


if __name__ == "__main__": # verify main method
    start_mashing_process()  # initiates mashing process
