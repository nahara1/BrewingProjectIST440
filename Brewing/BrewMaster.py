# Project: IST 440 Balrog Brewery
# Purpose Details: To develop a Brew Master class that holds the information to the BrewMaster
# Course: IST 440
# Author: Team Ferment
# Date Developed: 4/8/2020
# Last Date Changed: 4/8/2020
# Rev: 1


class BrewMaster:
    """
    This class has been written to obtain the Brew Master's needed credentials,
    as well as their corresponding Vessel ID.
    """
    def __init__(self, brew_master_id, name, vessel_id):
        self.brew_master_id = brew_master_id
        self.name = name
        self.vessel_id = vessel_id

# add getters


