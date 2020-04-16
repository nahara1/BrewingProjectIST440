# Project: IST 440 Barlog Brewery
# Course: IST 440
# Author: Team Ferment
# Date Developed: 4/6/20
# Last Date Changed: 4/6/20
# Rev: 1
import datetime
import random

random_temp = 0
import time
from Brewing.MongoLog import Log
import Brewing.BrewMaster


class FermentationVessel:

    def __init__(self, vessel_id, brew_master_id):
        self.vessel_id = vessel_id
        self.brew_master_id = brew_master_id

    def get_wort(self, batch_id):
        """
        Function for recieving the wort
        :param batch_id:
        :return: Return log
        """
        log = Log(1, "Receieving wort", "Recieved wort from Team Boil", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("-----------------------------------------")


    def add_to_fermentationVessel(vessel_id):
        """
        Function for adding the wort to fermentation vessel
        :param: vessel_id
        :return: Return log
        """

        log = Log(2, "Addition to Fermentation Vessel", "Adding wort to fermenation vessel ", datetime.datetime.now(),
                  "pass")
        print(log.generate_log())
        print("-----------------------------------------")


    def add_yeast(self):
        """
        Function for adding activated yeast to the fermentaiton vessel with wort
        :param: wort
        :return: Return Log
        """

        log = Log(3, "Ferment.addYeast", "Activated yeast has been added to the fermentation vessel",
                  datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("-----------------------------------------")


        return ("Yeast added")

    def close_lid(self):
        """
        Function for closing lid
        :param: Wort and yeast mixture
        :return: Return log
        """

        log = Log(4, "Ferment.closeLid", "Closing lid", datetime.datetime.now(), "pass")
        print(log.generate_log())
        print("-----------------------------------------")


    def begin_fermentation_process(self):
        """
        Function to begin fermentation process
        :param: wort and yeast mixture
        :return: return Log and brewed Ale
        """
        log = Log(5, "Ferment.beginFermentationProcess", "Beginning Fermentation Process", datetime.datetime.now(),
                  "pass")
        print(log.generate_log())
        print("-----------------------------------------")


        # for i in range(1):
        #  time.sleep(25)
        # print("Fermenting....")

    def drain_ale(self):
        """
        Function to drain Ale
        :param: Ale
        :return: Return log and filtered Ale
        """
        log = Log(5, "Ferment.drainAle", "Fermentation has completed. Draining Ale", datetime.datetime.now(), "pass")

        print(log.generate_log())

        print("-----------------------------------------")


    def qa(self, brew_master_id):
        """
        Function for quality testing 
        :param brew_master_id: 
        :return: pass or fail and Log 
        """

    print("QA")
    print("-----------------------------------------")


    def send_to_kegging(self):
        """
        Function to send filtered Ale to Team Kegging
        :param: Filter Ale
        :return: Return Log
        """

        print("-----------------------------------------")


    def main(self):
        vessel = FermentationVessel()
        vessel.beginFermentationProcess()

    if __name__ == '__main__':
        main()

