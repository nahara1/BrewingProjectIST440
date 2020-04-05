# Project: Brewing Project
# Purpose Details: Sparging tank transfer and automation
# Course: IST 440W
# Author: Team Mashing
# Date Developed: 3/17/2020
# Last Date Changed: 3/31/2020
# Rev: 1.3
import datetime
import time
from Log import Log
from TeamMashing.Wort import Wort
import pyglet

class SpargingTank: #constructor for class sparging tank
    def __init__(self, Sid,stir_time,water_temp,water_amt,heat_time, sparg_time, milled_amount):
        self.machine_id = Sid
        self.stirring_time = stir_time
        self.heating_time = heat_time
        self.water_amount = water_amt
        self.water_temp = water_temp
        self.sparging_time = sparg_time
        self.milled_grain_amount = milled_amount

    def add_milled_grains(self):
        #adding grains to the tank
        """
        Function for adding milled grains to the Sparging tank
        :param :milled Grain amount
        :return:Return log and animation
        """
        # log to end process
        log = Log(3, "Mashing.Sparging", "Milled grain added to tank", datetime.datetime.now(), "pass")
        print(log.generate_log())
        return "Milled Gains added to tank"
    def add_water(self):
        #adding heated water to tank
        """
        Water added to tank from hot liqor tank
        :param :Hot water from HLT
        :return: Return log and animation
        """
        log = Log(4, "Mashing.Sparging", "Heated water added to tank", datetime.datetime.now(), "pass")
        print(log.generate_log())
        return "Water pumped into tank"
    def stir_mash(self):
        #stirring the wort in progress
        """
        Function to stirr the Wort-inprogress sparging tank
        :param : Wort in HLT
        :return: Return log and animation
        """
        log = Log(3, "Mashing.Sparging", "Sparging Process Started", datetime.datetime.now(), "pass")
        print(log.generate_log())

        #sparging animation
        # ag_file = "mashwort.gif"
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

        stir_time = 10

        while stir_time > 0:
            print("Stirring Time Left: ", stir_time, "sec")
            time.sleep(1)
            stir_time -= 1

            if stir_time == 0:
                print ("SpargingTank stirred")

        log = Log(4, "Mashing.Sparging", "Sparging Process Ended", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("Mash Stirred")
        self.heat()

    def heat(self):
        #heat the tank for a defined time while stirring.
        """
        Function to heat the Sparging tank with Wort-inprogress inside
        :param : Wort in HLT
        :return: Return log and animation
        """
        log = Log(6, "Mashing.Sparging", "Wort heated", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("Proper tempature achieved")
        self.sparg_the_tank()

    def sparg_the_tank(self):
        #empty the tank while spraying water over the remaing grains.
        """
        Function to remove finished wort from Sparging tank.
        :param : Wort in HLT
        :return: Return log and animation
        """
        log = Log(7, "Mashing.Sparging", "Mash Sparged to Boiling", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("Tank emptying, washing grains.")
        w = Wort(4, 1, 1, 1, 1)
        w.separate_wort()