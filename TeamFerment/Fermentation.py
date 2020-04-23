# Project: IST 440 Balrog Brewery
# Purpose Details: To develop a main class that holds the information for the Fermentation process
# Course: IST 440
# Author: Team Ferment
# Date Developed: 4/6/20
# Last Date Changed: 4/18/20
# Rev: 2

from TeamFerment.FermentationVessel import FermentationVessel

import threading


def start_fermentation_process(request_number, recipe):
    fermentation_vessel = FermentationVessel(recipe)

    t1 = threading.Thread(target=fermentation_vessel.get_wort(request_number, recipe))

    t1.start()


#if __name__ == "__main__":
    #start_fermentation_process()
