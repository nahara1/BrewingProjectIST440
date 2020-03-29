# Project: Brewing Project
# Purpose Details: Automate wort process.
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 3/24/2020
# Rev: 1.2

import datetime
from Log import Log


class Wort:
    def __init__(self, wv, hotWaterTemp, waterVolume):
        self._wort_volume = wv
        self.HotWaterTemp = hotWaterTemp
        self.waterVolume = waterVolume
        self._wort_volume = False
        self.HotWater = False

        try:
            log = Log(1, "Wort.Received", "HotWater Received", datetime.datetime.now(), "Pass")
            print(log.generate_log())

            log = Log(2, "Mashing.Sparging", "Wort Generated", datetime.datetime.now(), "pass")
            print(log.generate_log())

        except Exception as e:
            print(e)
