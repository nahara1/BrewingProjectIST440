# Project: IST 440 Barlog Brewery
# Course: IST 440
# Author: Team Ferment
# Date Developed: 4/6/20
# Last Date Changed: 4/10/20
# Rev: 2

class FermentationVessel:

    def __init__(self, vessel_id, brew_master_id):
        self.vessel_id = vessel_id
        self.brew_master_id = brew_master_id

#Creating 5 vessel objects for different batches to ferment at the same time.
vessel1 = FermentationVessel(1)
vessel2 = FermentationVessel(2)
vessel3 = FermentationVessel(3)
vessel4 = FermentationVessel(4)
vessel5 = FermentationVessel(5)
vesselArray = [vessel1, vessel2, vessel3, vessel3, vessel4, vessel5]

    # def closeLid(self):
    # TODO: Add Code

    # def brewingComplete(self):
    # TODO: Add Code

    # def drainAle(self):
    # TODO: Add Code

    # def cleaningStatus(self):
    # TODO: Add Code
