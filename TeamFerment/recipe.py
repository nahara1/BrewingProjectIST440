# default constructor added
class Recipe:
    def __init__(self, id, name, volume, yeast, grain):
        self._id = None
        self._name = ""
        self._volume = 0.0
        self._yeast = None
        self._grain = None

    def getID(self):
        return self._id

    def setID(self):
        return self._id

    def getName(self):
        return self._name

    def setName(self):
        return self._name

    def getVolume(self):
        return self._volume

    def setVolume(self):
        return self._volume

    def getYeast(self):
        return self._yeast

    def setYeast(self):
        return self._yeast

    def getGrain(self):
        return self._grain

    def setGrain(self):
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