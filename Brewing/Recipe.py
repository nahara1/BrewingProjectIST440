# Project: IST 440 Barlog Brewery
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

    ''''''
    '''
        def __init__(self, recipe_id, name, volume, yeast_storage_amt, yeast, yeast_begin_temp, grain, sparge_time,
                 sparge_temp,
                 wort_volume, boil_temp, boil_time, add_hop_time, hop_amt, hops, after_boil_chill_temp, ferment_time,
                 add_yeast_time, add_yeast_temp, ferment_temp, wort_cool_temp, carbonation, bitter_units,
                 wort_cool_time, ferment_cool_temp):
        self._recipe_id = recipe_id
        self._name = name
        self._volume = volume
        self._yeast_store_amt = yeast_storage_amt
        self._yeast = yeast
        self._yeast_begin_temp = yeast_begin_temp
        self._grain = grain
        self._sparge_time = sparge_time
        self._sparge_temp = sparge_temp
        self._wort_volume = wort_volume
        self._boil_temp = boil_temp
        self._boil_time = boil_time
        self._add_hop_time = add_hop_time
        self._hop_amt = hop_amt
        self._hops = hops
        self._after_boil_chill_temp = after_boil_chill_temp
        self._ferment_time = ferment_time
        self._add_yeast_time = add_yeast_time
        self._add_yeast_temp = add_yeast_temp
        self._ferment_temp = ferment_temp
        self._wort_cool_temp = wort_cool_temp
        self._carbonation = carbonation
        self._bitter_units = bitter_units
        self._wort_cool_time = wort_cool_time
        self._ferment_cool_temp = ferment_cool_temp

    '''

    def __init__(self, recipe_id, name, abv, ibu, og, fg, batch_size, yeast_storage_amt, yeast, grain, water_volume,
                 water_temp, mill_time, sparge_time,
                 stir_time, hlt_heat_time, wort_separation_time, boil_temp, boil_duration, hop_schedule, hop_hop_amt,
                 after_boil_chill_temp,
                 ferment_time, ferment_temp, ferment_yeast_temp, wort_volume):
        self._recipe_id = recipe_id
        self._name = name
        self._batch_size = batch_size
        # Kegging and Ferment
        self._abv = abv
        self._ibu = ibu
        self._og = og
        self._fg = fg
        # Prep and Ferment
        self._yeast = yeast
        self._yeast_store_amt = yeast_storage_amt
        # Mashing and Prep
        self._mill_time = mill_time
        self._grain = grain
        self._water_volume = water_volume
        self._water_temp = water_temp
        self._sparge_time = sparge_time
        self._stir_time = stir_time
        self._hlt_heat_time = hlt_heat_time
        self._wort_separation_time = wort_separation_time
        self._wort_volume = wort_volume
        # Boiling
        self._boil_temp = boil_temp
        self._boil_time = boil_duration
        self._hop_schedule = hop_schedule
        self._hop_hop_amt = hop_hop_amt
        self._after_boil_chill_temp = after_boil_chill_temp
        # Ferment
        self._ferment_time = ferment_time
        self._ferment_temp = ferment_temp
        self._ferment_yeast_temp = ferment_yeast_temp

    def get_id(self):
        return self._recipe_id

    def get_name(self):
        return self._name

    def get_batch_size(self):
        return self._batch_size

    def get_abv(self):
        return self._abv

    def get_ibu(self):
        return self._abv

    def get_og(self):
        return self._og

    def get_fg(self):
        return self._fg

    def get_yeast_storage_amt(self):
        return self._yeast_store_amt

    def get_yeast(self):
        return self._yeast

    def get_grain(self):
        return self._grain

    def get_water_temp(self):
        return self._water_temp

    def get_water_volume(self):
        return self._water_volume

    def get_sparge_time(self):
        return self._sparge_time

    def get_hlt_heat_time(self):
        return self._hlt_heat_time

    def get_wort_separation_time(self):
        return self._wort_separation_time

    def get_stir_time(self):
        return self._stir_time

    # Boiling

    def get_boil_temp(self):
        return self._boil_temp

    def get_boil_time(self):
        return self._boil_time

    def get_hop_schedule(self):
        return self._hop_schedule

    def get_after_boil_chill_temp(self):
        return self._after_boil_chill_temp

    # Ferment
    def get_ferment_time(self):
        return self._ferment_time

    def get_ferment_temp(self):
        return self._ferment_temp

    def get_ferment_yeast_temp(self):
        return self._ferment_yeast_temp

    def get_grain_weight(self, grain):
        weight = 0
        for value in grain:
            weight = weight + value
        return weight

    def get_yeast_begin_temp(self):
        return self._yeast_begin_temp
        
    def get_hop_amt(self):
        return self._hop_hop_amt

    def get_add_hop_time(self):
        return self._add_hop_time
        
    def get_add_yeast_time(self):
        return self._add_yeast_time

    def get_add_yeast_temp(self):
        return self._add_yeast_temp

    def get_ferment_temp(self):
        return self._ferment_temp

    def get_wort_cool_temp(self):
        return self._wort_cool_temp

    def get_carbonation(self):
        return self._carbonation

    def get_bitter_units(self):
        return self._bitter_units

    def get_wort_cool_time(self):
        return self._wort_cool_time

    def get_ferment_cool_temp(self):
        return self._ferment_cool_temp

    def get_wort_volume(self):
        return self._wort_volume


