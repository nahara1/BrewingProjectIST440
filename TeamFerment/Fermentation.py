# Project: IST 440 Balrog Brewery
# Purpose Details: To develop a main class that holds the information for the Fermentation process
# Course: IST 440
# Author: Team Ferment
# Date Developed: 4/6/20
# Last Date Changed: 4/6/20
# Rev: 1

from TeamFerment.FermentationVessel import FermentationVessel

import threading



class main:

    fermentation_vessel = FermentationVessel()

    t1 = threading.Thread(target=fermentation_vessel.get_wort(123))

    t1.start()



if __name__ == "__main__":
    main()