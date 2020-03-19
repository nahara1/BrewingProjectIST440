# Project: Brewing Project
# Purpose Details: Enumerator for conditions.
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 3/18/2020
# Rev: 1.1

import enum

class Process(enum.Enum):
    Prep = 1
    Mash = 2
    Boil = 3
    Ferment = 4
    Keg = 5