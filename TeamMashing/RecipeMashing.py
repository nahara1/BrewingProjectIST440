from Brewing import BrewRequest

class recipe_mashing():
    """These will be set to the ServiceNow Recipe."""
    mill_time = BrewRequest.get_recipe(BrewRequest.get_recipe()).get_mill_time()
    grains_weight = BrewRequest.get_recipe(BrewRequest.get_recipe().get_name()).get_grains_weight()
    water_amount = BrewRequest.get_recipe(BrewRequest.get_recipe().get_name()).get_water_volume()
    water_temp = BrewRequest.get_recipe(BrewRequest.get_recipe().get_name()).get_water_temp()
    stir_time = BrewRequest.get_recipe(BrewRequest.get_recipe().get_name()).get_wort_stir_time()
    heating_time = BrewRequest.get_recipe(BrewRequest.get_recipe().get_name()).get_hlt_heat_time()
    sparging_time = BrewRequest.get_recipe(BrewRequest.get_recipe().get_name()).get_sparge_time()
    wort_volume = BrewRequest.get_recipe(BrewRequest.get_recipe().get_name()).get_wort_volume()
    separation_time = BrewRequest.get_recipe(BrewRequest.get_recipe().get_name()).get_separation_time()
