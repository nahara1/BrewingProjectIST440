from Brewing import BrewRequest

class recipe_mashing:
    mill_time = 10
    grains_weight = BrewRequest.get_recipe().get_grain()
    water_amount = BrewRequest.get_recipe().get_volume()
    water_temp = 140
    stir_time = 10
    heating_time = 10
    sparging_time = BrewRequest.get_recipe().get_sparge_time()
    wort_volume = BrewRequest.get_recipe().get_wort_volume()
    separation_time = 10
