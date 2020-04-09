# Project: Brewing Project
# Purpose Details: Automate milling machine process
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 3/31/2020
# Rev: 1.2

import datetime
import time

from Brewing.MongoLog import Log
from TeamMashing.SpargingTank import SpargingTank


class MillingMachine:  # MillingMachine Start
    def __init__(self, mid, mt):  # constructor initalized fields
        self.machine_id = mid
        self.mill_time = mt
        self.is_milled = False
        self.is_transferred = False

    def mill_grains(self):  # Mill_grains process start
        """
        The start of milling grains
        :param mid: machine id
        :param mt: milling time
        :param ismilled: milling completes (bool)
        :param istransferred: transfer indication (bool)
        :return: Return Log and animation of milling grains
        """
        try:
            # log to begin process
            log = Log(1, "Mashing.Milling", "Milling Started", datetime.datetime.now(), "pass")
            print(log.generate_log())

            # mill grains animation
            # ag_file = "millgrains.gif"
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

            mt = 10

            while mt > 0:
                print("Milling Time Left: ", mt, "sec")
                time.sleep(1)
                mt -= 1

                if mt == 0:
                    print("Grains milled")

            # log to end process
            log = Log(2, "Mashing.Milling", "Milling Ended", datetime.datetime.now(), "pass")
            print(log.generate_log())
            self.send_grains_to_sparging_tank(self)
        except Exception as e:  # error handling
            print(e)

    def send_grains_to_sparging_tank(self, s):
        # sends grains to Sparging Tank
        """
        grains are added to the Sparging Tank
        :param
        :return: print statement
        """
        print("Grains added to Sparging Tank")
        s = SpargingTank(3, 10, 1, 1, 1, 1, 1)
        s.stir_mash()
