# Project: IST 440 Barlog Brewery
# Course: IST 440
# Author: Team Ferment
# Date Developed: 4/6/20
# Last Date Changed: 4/6/20
# Rev: 1
import random
random_temp = 0
class FermentationVessel:

    def __init__(self, vessel_id, brew_master_id):
        self.vessel_id = vessel_id
        self.brew_master_id = brew_master_id

        def getWort(self,batch_id):
            print("Wort recieved from boiling")


        def addToFermentationVessel(vessel_id):
            print("Wort added to vessel" + vessel_id)

        def addYeast(self):
            print ("Yeast added")
        def closeLid(self):
            print("Begin to close lid")

        def setTemperature(self):
            for x in range(1):
                random_temp = random.randint(67,73)
                print("Temperture is set at: " + random_temp)


         def setTime(self):
             
        #drainAle(self)
        #QA(self, brew_master_id)
        #sendToKegging(self)

    # def closeLid(self):
    # TODO: Add Code

    # def brewingComplete(self):
    # TODO: Add Code

    # def drainAle(self):
    # TODO: Add Code

    # def cleaningStatus(self):
    # TODO: Add Code
