# Project: Brewing Project
# Purpose Details: Automate wort process.
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 3/31/2020
# Rev: 1.3

import datetime
from Log import Log


class Wort:
    def __init__(self, wid, wortvolume, hotWaterTemp, waterVolume):
        self.wort_id = wid
        self._wort_volume = wortvolume
        self.HotWaterTemp = hotWaterTemp
        self.waterVolume = waterVolume
        self._wort_volume = False
        self.HotWater = False

    def wortVolume(self):
        # Sets and displays wort volume
        """
        :type :float
        :param float: shows correct wort volume
        :return: Return log and animation of wort processes
        """
        # Records correct wort volume to Log and show animation
        log = Log(2, "Mashing.Wort", "Wort Transferred", datetime.datetime.now(), "pass")
        print(log.generate_log())
        return "Wort Volume"


    def HotWaterTemp(self):
        # Sets and displays the correct water temperature
        """
        :param int: displays correct water temp
        :return :Return Log and animation of wort processes
        """
        # Records correct hot water temp to Log and show animation
        log = Log(1, "Mashing.Wort", "Wort transferred", datetime.datetime.now(), "pass")
        print(log.generate_log())
        return "Displays Hot Water Temperature"

    def water_volume(self):
        # Displays the correct water volume
        """
        :param current_water_volume: get the correct water volume
        :param set_correct_water_volume: set the correct water volume
        :param :transfer correct water volume
        :return: Return Log and animation of wort processes
        """
        log = Log(1, "Mashing.Wort", "Water Volume", datetime.datetime.now(), "pass")
        print(log.generate_log())
        return "Water Volume"