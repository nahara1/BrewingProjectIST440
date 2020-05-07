# Project: IST 440 Barlog Brewery
# Course: IST 440
# Author: Team Ferment
# Date Developed: 4/6/20
# Last Date Changed: 4/23/20
# Rev: 5

import datetime
import random
import time
from Brewing.Log import Log
from Brewing import Recipe
from Brewing import ServiceNowLog
from Brewing import MongoLogging
import Brewing.BrewMaster
import sys
sleep_time = .5

class FermentationVessel:

    def __init__(self, recipe):
        self.vessel_id = 1
        self.brew_master_id = 2
        self.ferment_time = recipe.get_ferment_time()
        self.ferment_temp = recipe.get_ferment_temp()
        self.original_gravity = recipe.get_og()
        self.final_gravity = recipe.get_fg()
        self.base_abv = recipe.get_abv()

    def get_wort(self, request_number):
        """
        Function for receiving the wort
        :param request_number: the ID of the current batch
        :return: Return log
        """

        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Fermentation\", \"log\":\"Starting Fermentation Process\"}"
        ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
        log = Log(1, "Receiving wort", "Received wort from Team Boil", datetime.datetime.now(), "pass")
        print(log.generate_log())
        ml = MongoLogging.MongoLogging()
        MongoLogging.MongoLogging.MongoLog(ml, request_number, "Fermentation", "Starting Fermentation Process")
        print("-----------------------------------------")
        self.add_to_fermentation_vessel(request_number)

    def add_to_fermentation_vessel(self, request_number):
        """
        Function for adding the wort to fermentation vessel
        :param: vessel_id : the ID of the vessel
        :return: Return log
        """
        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Fermentation\", \"log\":\"Wort added to Vessel\"}"
        ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
        log = Log(2, "Addition to Fermentation Vessel", "Adding wort to fermentation vessel ", datetime.datetime.now(),
                  "pass")
        print(log.generate_log())
        ml = MongoLogging.MongoLogging()
        MongoLogging.MongoLogging.MongoLog(ml, request_number, "Fermentation", "Wort added to Fermentation Vessel")
        print("-----------------------------------------")
        self.measure_original_gravity(request_number)

    def measure_original_gravity(self, request_number):
        """
        Function for taking the original gravity (OG) reading of the mixture
        :param: self
        :return: Return log
        """
        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Fermentation\", \"log\":\"Measuring Original Gravity\"}"
        ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
        log = Log(3, "Ferment.Measure Original Gravity", "Measuring original gravity ", datetime.datetime.now(),
                  "pass")
        print(log.generate_log())
        base_measurement = 0
        try:
            while base_measurement < self.original_gravity:
                print("Measuring: ", base_measurement, "g/mL")  # grams per milli-Liter
                time.sleep(sleep_time)
                base_measurement += 0.050
                if base_measurement == self.original_gravity:
                    print("Original Gravity has been measured")
                    print("-----------------------------------------")
                    log = Log(4, "Ferment.MeasureOriginalGravity", " Original gravity measured ",
                              datetime.datetime.now(),
                              "pass")
                    print(log.generate_log())
        except Exception as ex:
            print(ex)
        ml = MongoLogging.MongoLogging()
        MongoLogging.MongoLogging.MongoLog(ml, request_number, "Fermentation", "Measured Original Gravity")
        print("-----------------------------------------")
        self.add_yeast(request_number)

    def get_original_gravity(self):
        """
        Function for getting the OG of the mixture
        :param: self
        :return: Return Log
        """
        return self.original_gravity

    def add_yeast(self, request_number):
        """
        Function for adding activated yeast to the fermentation vessel with wort
        :param: self
        :return: Return Log
        """
        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Fermentation\", \"log\":\"Adding yeast to vessel\"}"
        ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
        log = Log(5, "Ferment.addYeast", "Activated yeast has been added to the fermentation vessel",
                  datetime.datetime.now(), "pass")
        print(log.generate_log())
        ml = MongoLogging.MongoLogging()
        MongoLogging.MongoLogging.MongoLog(ml, request_number, "Fermentation", "Adding Yeast to Fermentation Vessel")
        print("-----------------------------------------")
        self.close_lid(request_number)
        return ("Yeast added")

    def close_lid(self, request_number):
        """
        Function for closing lid
        :param: self
        :return: Return log
        """
        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Fermentation\", \"log\":\"Closing lid of vessel\"}"
        ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
        log = Log(6, "Ferment.closeLid", "Closing lid", datetime.datetime.now(), "pass")
        print(log.generate_log())
        ml = MongoLogging.MongoLogging()
        MongoLogging.MongoLogging.MongoLog(ml, request_number, "Fermentation", "Closing Fermentation Vessel Lid")
        print("-----------------------------------------")
        self.begin_fermentation_process(request_number)

    def set_ferment_temperature(self, request_number):
        """
        Function for setting the temperature of the mixture to ferment
        :param: self
        :return: Return fermentation temperature
        """
        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Fermentation\", \"log\":\" Setting fermentation temperature\"}"
        ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
        log = Log(7, "Ferment.setFermentTemperature",
                  "Temperature is set at %.2f" % self.ferment_temp,
                  datetime.datetime.now(), "pass")
        print(log.generate_log())
        ml = MongoLogging.MongoLogging()
        MongoLogging.MongoLogging.MongoLog(ml, request_number, "Fermentation", "Setting Fermentation Temperature")
        print("-----------------------------------------")
        self.begin_fermentation_process(request_number)

    def begin_fermentation_process(self, request_number):
        """
        Function to begin fermentation process
        :param: self
        :return: return Log and brewed Ale
        """
        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Fermentation\", \"log\":\" Fermentation had begun\"}"
        ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
        log = Log(7, "Ferment.beginFermentationProcess", "Beginning Fermentation Process", datetime.datetime.now(),
                  "pass")
        print(log.generate_log())
        try:
            while self.ferment_time > 0:
                print("Fermentation time Left: ", self.ferment_time, "sec")
                time.sleep(sleep_time)
                self.ferment_time -= 1
                if self.ferment_time == 0:
                    print("Fermentation has completed")
                    print("-----------------------------------------")
                    log = Log(8, "Ferment.beginFermentationProcess", "Fermentation has completed",
                              datetime.datetime.now(),
                              "pass")
                    print(log.generate_log())
        except Exception as ex:
            print(ex)
        ml = MongoLogging.MongoLogging()
        MongoLogging.MongoLogging.MongoLog(ml, request_number, "Fermentation", "Fermentation has begun")
        print("-----------------------------------------")
        self.measure_final_gravity(request_number)

    def measure_final_gravity(self, request_number):
        """
        Function to measure the final gravity (FG) of the mixture
        :param: self
        :return: return Log
        """
        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Fermentation\", \"log\":\" Measuring Final Gravity\"}"
        ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
        log = Log(9, "Ferment.FinalGravity", "Measuring Final Gravity", datetime.datetime.now(), "pass")
        print(log.generate_log())
        base_measurement = 0
        try:
            while base_measurement < self.final_gravity:
                print("Measuring Final Gravity: ", base_measurement, "g/mL")  # grams per milli-Liter
                time.sleep(sleep_time)
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
        ml = MongoLogging.MongoLogging()
        MongoLogging.MongoLogging.MongoLog(ml, request_number, "Fermentation", "Measured Final Gravity")
        print("-----------------------------------------")
        self.drain_ale(request_number)

    def get_final_gravity(self):
        return self.final_gravity

    def drain_ale(self, request_number):
        """
        Function to drain Ale
        :param: self
        :return: Return log and filtered Ale
        """
        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Fermentation\", \"log\":\"Draining Ale\"}"
        ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
        log = Log(11, "Ferment.drainAle", "Draining Ale. Sending to QA", datetime.datetime.now(), "pass")
        print(log.generate_log())
        ml = MongoLogging.MongoLogging()
        MongoLogging.MongoLogging.MongoLog(ml, request_number, "Fermentation", "Draining Ale")
        print("-----------------------------------------")
        self.qa(self.brew_master_id, request_number)

    def qa(self, brew_master_id, request_number):
        """
        Function for quality testing
        :param brew_master_id: the ID of the brew master
        :return: pass or fail and Log
        """
        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Fermentation\", \"log\":\"Checking Quality Assurance\"}"
        ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
        log = Log(12, "Ferment.QualityAssurance", "Quality Assurance", datetime.datetime.now(), "fail")
        print(log.generate_log())
        try:
            difference = self.final_gravity - self.original_gravity
            measured_abv = (difference * 131.25)
            abs(measured_abv) == measured_abv
            if measured_abv == self.base_abv:
                log = Log(13, "Ferment.QualityAssurance", "Quality Assurance", datetime.datetime.now(), "pass")
                print(log.generate_log())
        except Exception as e:
            print(e)
        ml = MongoLogging.MongoLogging()
        MongoLogging.MongoLogging.MongoLog(ml, request_number, "Fermentation", "Checked Quality Assurance")
        print("-----------------------------------------")
        self.send_to_kegging(request_number)

    def send_to_kegging(self, request_number):
        """
        Function to send filtered Ale to Team Kegging
        :param: self
        :return: Return Log
        """
        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Fermentation\", \"log\":\"Sending Ale to the Kegging Process\"}"
        ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
        log = Log(13, "Ferment.send_to_kegging", "Ale sent to kegging", datetime.datetime.now(), "pass")
        print(log.generate_log())
        ml = MongoLogging.MongoLogging()
        MongoLogging.MongoLogging.MongoLog(ml, request_number, "Fermentation", "Sending Ale to the Kegging Process")
        print("-----------------------------------------")

    def sanitization(self, request_number):
        status_log = "{\"batch_id\":\"" + request_number + "\", \"brew_batch_stage\":\"Fermentation\", \"log\":\"Sanitizing Vessel\"}"
        ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
        log = Log(14, "Ferment.sanitize_vessels", datetime.datetime.now(), "pass")
        print(log.generate_log())
        ml = MongoLogging.MongoLogging()
        MongoLogging.MongoLogging.MongoLog(ml, request_number, "Fermentation", "Sanitizing Vessels")
        print("-----------------------------------------")
