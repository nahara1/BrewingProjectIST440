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
        return self.recipe_id

    def get_name(self):
        return self.name

    def get_batch_size(self):
        return self.batch_size

    def get_abv(self):
        return self.abv

    def get_ibu(self):
        return self.ibu

    def get_og(self):
        return self.og

    def get_fg(self):
        return self.fg

    def get_yeast_storage_amt(self):
        return self.yeast_store_amt

    def get_yeast(self):
        return self.yeast

    def get_grain(self):
        return self.grain

    def get_water_temp(self):
        return self.water_temp

    def get_water_volume(self):
        return self.water_volume

    def get_sparge_time(self):
        return self.sparge_time

    def get_hlt_heat_time(self):
        return self.hlt_heat_time

    def get_wort_separation_time(self):
        return self.wort_separation_time

    def get_stir_time(self):
        return self.stir_time

    # Boiling

    def get_boil_temp(self):
        return self.boil_temp

    def get_boil_time(self):
        return self.boil_time

    def get_hop_schedule(self):
        return self.hop_schedule

    def get_after_boil_chill_temp(self):
        return self.after_boil_chill_temp

    # Ferment
    def get_ferment_time(self):
        return self.ferment_time

    def get_ferment_temp(self):
        return self.ferment_temp

    def get_grain_weight(self, grain):
        weight = 0
        float(weight)

        for value in grain.values():
            str(value).replace("<", "")
            value = float(value)
            weight = weight + value
        return weight

    def get_hop_hop_amt(self):
        return self.hop_hop_amt

    def get_hops_weight(self, hop_hop_amt):
        weight = 0
        for value in hop_hop_amt.values():
            str(value).replace("<", "")
            value = float(value)
            weight = weight + value
        return weight

    def get_add_hop_time(self):
        return self.add_hop_time

    def get_add_yeast_time(self):
        return self.add_yeast_time

    def get_add_yeast_temp(self):
        return self.add_yeast_temp

    def get_wort_cool_time(self):
        return self.wort_cool_time

    def get_wort_volume(self):
        return self.wort_volume

    def get_mill_time(self):
        return self.mill_time
