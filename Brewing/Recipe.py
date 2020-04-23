# Project: IST 440 Balrog Brewery
# Purpose Details: To create a Recipe Class, used by each to retrieve information about the Lager's recipe.
# Course: IST 440
# Author: Team Ferment
# Date Developed: 3/16/2020
# Last Date Changed: 4/18/2020
# Rev: 6

# default constructor added


class Recipe:
    """
    This class was written to be used by each team. All of the attributes are available to be obtained by getters.
    """
    recipe_id = 0

    def __init__(self, recipe_id, name, abv, ibu, og, fg, batch_size, yeast_storage_amt, yeast, grain, water_volume,
                 water_temp, mill_time, sparge_time,
                 stir_time, hlt_heat_time, wort_separation_time, boil_temp, boil_duration, hop_schedule, hop_hop_amt,
                 after_boil_chill_temp,
                 ferment_time, ferment_temp, wort_volume):
        """
        Recipe Constructor
        :param recipe_id: recipe id
        :param name: recipe name
        :param abv: recipe ABV
        :param ibu: recipe IBU
        :param og: recipe OG
        :param fg: rccipe FG
        :param batch_size: rccipe batch size
        :param yeast_storage_amt: rccipe yeast storage amount
        :param yeast: recipe yeast
        :param grain: recipe grain bill listing grains and weights
        :param water_volume: recipe water volume
        :param water_temp: recipe water temperature
        :param mill_time: recipe mill time
        :param sparge_time: recipe sparge time
        :param stir_time: recipe stir time
        :param hlt_heat_time: recipe HLT heat time
        :param wort_separation_time: recipe wort separation time
        :param boil_temp: recipe boil temperature
        :param boil_duration: recipe boil duration
        :param hop_schedule: recipe hop addition times schddule
        :param hop_hop_amt: recipe hops and weight
        :param after_boil_chill_temp: recipe wort chill temperature
        :param ferment_time: recipe fermentation time
        :param ferment_temp: recipe fermentation temperature
        :param wort_volume: recipe wort volume
        """
        self.recipe_id = recipe_id
        self.name = name
        self.batch_size = batch_size
        # Kegging and Ferment
        self.abv = abv
        self.ibu = ibu
        self.og = og
        self.fg = fg
        # Prep and Ferment
        self.yeast = yeast
        self.yeast_store_amt = yeast_storage_amt
        # Mashing and Prep
        self.mill_time = mill_time
        self.grain = grain
        self.water_volume = water_volume
        self.water_temp = water_temp
        self.sparge_time = sparge_time
        self.stir_time = stir_time
        self.hlt_heat_time = hlt_heat_time
        self.wort_separation_time = wort_separation_time
        self.wort_volume = wort_volume
        # Boiling
        self.boil_temp = boil_temp
        self.boil_time = boil_duration
        self.hop_schedule = hop_schedule
        self.hop_hop_amt = hop_hop_amt
        self.after_boil_chill_temp = after_boil_chill_temp
        # Ferment
        self.ferment_time = ferment_time
        self.ferment_temp = ferment_temp

    def get_id(self):
        """
        Gets Recipe ID
        :return: recipe id
        """
        return self.recipe_id

    def get_name(self):
        """
        Gets Recipe Name
        :return: recipe name
        """
        return self.name

    def get_batch_size(self):
        """
        Gets the batch size
        :return: Recipe batch size
        """
        return self.batch_size

    def get_abv(self):
        """
        Gets ABV
        :return: Recipe ABV level
        """
        return self.abv

    def get_ibu(self):
        """
        Gets IBU
        :return: Recipe International Bitter Units
        """
        return self.ibu

    def get_og(self):
        """
        Gets original gravity
        :return: original gravity
        """
        return self.og

    def get_fg(self):
        """
        Gets Final Gravity
        :return: Recipe final gravity
        """
        return self.fg

    def get_yeast_storage_amt(self):
        """
        Gets yeast storage amount
        :return: yeast amount
        """
        return self.yeast_store_amt

    def get_yeast(self):
        """
        Gets Yest
        :return: yeast
        """
        return self.yeast

    def get_grain(self):
        """
        Gets dictionary of grains and corresponding measures
        :return: a grains dictionary of types and measures
        """
        return self.grain

    def get_water_temp(self):
        """
        Gets water temperature
        :return: water temperature
        """
        return self.water_temp

    def get_water_volume(self):
        """
        Gets water volume
        :return: water volume
        """
        return self.water_volume

    def get_sparge_time(self):
        """
        Gets sparge time
        :return: sparge time
        """
        return self.sparge_time

    def get_hlt_heat_time(self):
        """
        Gets Hot Liquor Tank heat time
        :return: HLT heat time
        """
        return self.hlt_heat_time

    def get_wort_separation_time(self):
        """
        Gets wort separation time
        :return: wort separation time
        """
        return self.wort_separation_time

    def get_stir_time(self):
        """
        Gets stirring time
        :return: stir time
        """
        return self.stir_time

    # Boiling

    def get_boil_temp(self):
        """
        Gets boil temperature
        :return: boil temperature
        """
        return self.boil_temp

    def get_boil_time(self):
        """
        Gets boil time
        :return: boil time
        """
        return self.boil_time

    def get_hop_schedule(self):
        """
        Gets hop schedule
        :return: a dictionary of hops and times to add them
        """
        return self.hop_schedule

    def get_after_boil_chill_temp(self):
        return self.after_boil_chill_temp

    # Ferment
    def get_ferment_time(self):
        """
        Gets fermentation time
        :return: ferment time
        """
        return self.ferment_time

    def get_ferment_temp(self):
        """
        Gets fermentation temperature
        :return: fermentation temperature
        """
        return self.ferment_temp

    def get_grain_weight(self, grain):
        """
        Gets the recipe total weight of grains
        :param grain: a grains bill dictionary
        :return: total weight of grains
        """
        weight = 0
        float(weight)

        for value in grain.values():
            str(value).replace("<", "")
            value = float(value)
            weight = weight + value
        return weight

    def get_hop_hop_amt(self):
        """
        Gets hops names and respective amounts
        :return: a dictionary of hops and respective weights
        """
        return self.hop_hop_amt

    def get_hops_weight(self, hop_hop_amt):
        """
        Gets total hops weight
        :param hop_hop_amt: a dictionary of hops and respective weights
        :return: total hops weight
        """
        weight = 0
        for value in hop_hop_amt.values():
            str(value).replace("<", "")
            value = float(value)
            weight = weight + value
        return weight

    def get_add_yeast_time(self):
        """
        Gets yeast addition time
        :return: yeast addition time
        """
        return self.add_yeast_time

    def get_add_yeast_temp(self):
        """
        Gets yeast temperature
        :return: yeast temperature
        """
        return self.add_yeast_temp

    def get_after_boil_chill_temp(self):
        """
        Gets wort chil temperature
        :return: expected after boil work temperature
        """
        return self.after_boil_chill_temp

    def get_wort_volume(self):
        """
        Gets desired wort volume
        :return: desired wort volume
        """
        return self.wort_volume

    def get_mill_time(self):
        """
        Gets milling time
        :return: milling time
        """
        return self.mill_time
