# Project: IST 440 Barlog Brewery
# Course: IST 440
# Author: Team Ferment
# Date Developed: 4/6/20
# Last Date Changed: 4/17/20
# Rev: 3
import datetime
import random
random_temp = 0
import time
from Brewing.Log import Log
import Brewing.BrewMaster

class FermentationVessel:
    def __init__(self):
        self.vessel_id = 1
        self.brew_master_id = 345
        self.fermentation_time = 5
        self.original_gravity = 1.05
        self.final_gravity = 1.01
        self.base_abv = 5.25
    def get_wort(self, batch_id):
        """
        Function for receiving the wort
        :param batch_id: the ID of the current batch
        :return: Return log
        """
        log = Log(1, "Receiving wort", "Received wort from Team Boil", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("-----------------------------------------")
        self.add_to_fermentation_vessel(vessel_id=1)

    def add_to_fermentation_vessel(self, vessel_id):
        """
        Function for adding the wort to fermentation vessel
        :param: vessel_id : the ID of the vessel
        :return: Return log
        """
        log = Log(2, "Addition to Fermentation Vessel", "Adding wort to fermentation vessel ", datetime.datetime.now(),
                  "pass")
        print(log.generate_log())
        print("-----------------------------------------")
        self.measure_original_gravity()

    def measure_original_gravity(self):
        """
        Function for taking the original gravity (OG) reading of the mixture
        :param: self
        :return: Return log
        """
        log = Log(3, "Ferment.Measure Original Gravity", "Measuring original gravity ", datetime.datetime.now(),
                  "pass")
        print(log.generate_log())
        base_measurement = 0
        try:
            while  base_measurement < self.original_gravity:
                print("Measuring: ",  base_measurement, "g/mL") # grams per milli-Liter
                time.sleep(1)
                base_measurement +=0.050
                if base_measurement == self.original_gravity:
                    print("Original Gravity has been measured")
                    print("-----------------------------------------")
                    log = Log(4, "Ferment.MeasureOriginalGravity", " Original gravity measured ",
                              datetime.datetime.now(),
                              "pass")
                    print(log.generate_log())
        except Exception as ex:
            print(ex)
        print("-----------------------------------------")
        self.add_yeast()

    def get_original_gravity(self):
        """
        Function for getting the OG of the mixture
        :param: self
        :return: Return Log
        """
        return self.original_gravity


    def add_yeast(self):
        """
        Function for adding activated yeast to the fermentation vessel with wort
        :param: self
        :return: Return Log
        """
        log = Log(5, "Ferment.addYeast", "Activated yeast has been added to the fermentation vessel",
                  datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("-----------------------------------------")
        self.close_lid()

        return ("Yeast added")


    def close_lid(self):
        """
        Function for closing lid
        :param: self
        :return: Return log
        """
        log = Log(6, "Ferment.closeLid", "Closing lid", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("-----------------------------------------")
        self.begin_fermentation_process()

    def set_ferment_temperature(self):
        """
        Function for setting the temperature of the mixture to ferment
        :param: self
        :return: Return fermentation temperature
        """
        log = Log(7, "Ferment.setFermentTemperature", "Temperature is set at %.2f" % self.sample_ferment_tempertature, datetime.datetime.now(), "pass")
        print(log.generate_log())
        self.begin_fermentation_process()

    def begin_fermentation_process(self):
        """
        Function to begin fermentation process
        :param: self
        :return: return Log and brewed Ale
        """
        log = Log(7, "Ferment.beginFermentationProcess", "Beginning Fermentation Process", datetime.datetime.now(),
                  "pass")
        print(log.generate_log())

        try:
            while self.fermentation_time > 0:
                print("Fermentation time Left: ", self.fermentation_time, "sec")
                time.sleep(1)
                self.fermentation_time -= 1
                if self.fermentation_time == 0:
                    print("Fermentation has completed")
                    print("-----------------------------------------")
                    log = Log(8, "Ferment.beginFermentationProcess", "Fermentation has completed",
                              datetime.datetime.now(),
                              "pass")
                    print(log.generate_log())
        except Exception as ex:
            print(ex)
        print("-----------------------------------------")
        self.measure_final_gravity()

    def measure_final_gravity(self):
        """
        Function to measure the final gravity (FG) of the mixture
        :param: self
        :return: return Log
        """
        log = Log(9, "Ferment.FinalGravity", "Measuring Final Gravity", datetime.datetime.now(), "pass")
        print(log.generate_log())
        base_measurement = 0
        try:
            while base_measurement < self.final_gravity:
                print("Measuring Final Gravity: ", base_measurement, "g/mL") # grams per milli-Liter
                time.sleep(1)
                base_measurement += 0.050
                if base_measurement == self.final_gravity:
                    print("Final Gravity has been measured")
                    print("-----------------------------------------")
                    log = Log(10, "Ferment.MeasureFinalGravity", " Final gravity measured ",
                              datetime.datetime.now(),
                              "pass")
                    print(log.generate_log())
        except Exception as ex:
            print(ex)
        print("-----------------------------------------")
        self.drain_ale()

    def get_final_gravity(self):
        return self.final_gravity

    def drain_ale(self):
        """
        Function to drain Ale
        :param: self
        :return: Return log and filtered Ale
        """
        log = Log(11, "Ferment.drainAle", "Draining Ale. Sending to QA", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("-----------------------------------------")
        self.qa(1)


    def qa(self, brew_master_id):
        """
        Function for quality testing
        :param brew_master_id: the ID of the brew master
        :return: pass or fail and Log
        """
        log = Log(12, "Ferment.QualityAssurance", "Quality Assurance", datetime.datetime.now(), "fail")
        print(log.generate_log())
        try:
            difference = self.final_gravity - self.original_gravity
            measured_abv = (difference*131.25)
            abs(measured_abv) == measured_abv
            if measured_abv == self.base_abv:
                log = Log(13, "Ferment.QualityAssurance", "Quality Assurance", datetime.datetime.now(), "pass")
                print(log.generate_log())
        except Exception as e:
            print(e)

        print("-----------------------------------------")
        self.send_to_kegging()


    def send_to_kegging(self):
        """
        Function to send filtered Ale to Team Kegging
        :param: self
        :return: Return Log
        """
        log = Log(13, "Ferment.send_to_kegging", "Ale sent to kegging", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("-----------------------------------------")


