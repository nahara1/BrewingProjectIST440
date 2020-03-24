
#Project: IST 440 Barlog Brewery 
#Purpose Details: To create a Recipe Class 
#Course: IST 440 
#Author: Asraa Alkurdi, Jinal Parmar, Anny Espinal 
#Date Developed: 3/16/2020
#Last Date Changed: 3/19/2020
#Rev: 3

# default constructor added
class Recipe:
    def __init__(self, id, name, volume, yeast, grain):
        self._id = id
        self._name = name
        self._volume = volume
        self._yeast = yeast
        self._grain = grain

    def get_id(self):
        return self._id

    def set_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self):
        return self._name

    def get_volume(self):
        return self._volume

    def set_volume(self):
        return self._volume

    def getYeast(self):
        return self._yeast

    def set_yeast(self):
        return self._yeast

    def get_grain(self):
        return self._grain

    def set_grain(self):
        return self._grain

# attributes
# _recipe_id = None
# _recipe_name = ""
# _recipe_volume = 0.0
# _recipe_yeast_storage_amt = 0.0
# _recipe_yeast = None
# _recipe_yeast_begin_temp = 0.0
# _recipe_grain = None
# _recipe_sparge_time = 0.0
# _recipe_sparge_temp = 0.0
# _recipe_wort_volume = 0.0
# _recipe_boil_temp = 0.0
# _recipe_boil_time = 0.0
# _recipe_add_hop_time = 0.0
# _recipe_hop_amt = 0.0
# _recipe_hops = None
# _recipe_after_boil_chill_temp = 0.0
# _recipe_ferment_time = 0.0
# _recipe_add_yeast_time = 0.0
# _recipe_add_yeast_temp = 0.0
# _recipe_ferment_temp = 0.0
# _recipe_wort_cool_temp = 0.0
# _recipe_carbonation = 0.0
# _recipe_bitter_units = 0.0
# _recipe_wort_cool_time = 0.0
# _recipe_wort_cool_temp = 0.0
# _recipe_ferment__cool_temp = 0.0
