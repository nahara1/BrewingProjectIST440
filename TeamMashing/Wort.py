# Project: Brewing Project
# Purpose Details: Automate wort process.
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 3/31/2020
# Rev: 1.3

import datetime
import time
from Brewing.MongoLog import Log


class Wort:
    def __init__(self, wid, wortvolume, hotWaterTemp, waterVolume, st):
        self.wort_id = wid
        self._wort_volume = wortvolume
        self.HotWaterTemp = hotWaterTemp
        self.waterVolume = waterVolume
        self.separation_time = st
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

    def separate_wort(self):
        # Separates the wort from the mash
        """
        :return: Return Log and animation
        """
        log = Log(4, "Mashing.Wort", "Wort Separation Started", datetime.datetime.now(), "pass")
        print(log.generate_log())

        # wort sepration animation
        # ag_file = "filtermash.gif"
        # animation = pyglet.resource.animation(ag_file)
        # sprite = pyglet.sprite.Sprite(animation)
        # win = pyglet.window.Window(width=sprite.width, height=sprite.height)
        # green = 0, 1, 0, 1
        # pyglet.gl.glClearColor(*green)

        # @win.event
        # def on_draw():
            # win.clear()
            # sprite.draw()

        # pyglet.app.run()

        st = 10

        while st > 0:
            print("Wort Separating Time Left: ", st, "sec")
            time.sleep(1)
            st -= 1

            if st == 0:
                print("Wort Separation Completed")

        log = Log(4, "Mashing.Wort", "Wort Separation Ended", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("Wort Separated from Mash")
