
from Brewing import Recipe
from Brewing import Brew
from Brewing import BrewRequest
from Brewing import BrewBatch
from TeamFerment import Fermentation
from TeamPrep import Sanitization
from TeamPrep import Temperature
from TeamPrep import WeightScale
from TeamPrep import QualityCheck_Prep
from TeamPrep import Prep_Main
from Brewing import BrewBatchStage
from TeamMashing import MillingMachine
import datetime
from TeamBoiling import Boil
from TeamKegging.KeggingMain import KeggingMain
from TeamFerment.Fermentation import start_fermentation_process
from Brewing import Log
import sys
import time
import threading


def main():
    # Get a brew request

    try:
        # 1 - Get brew request id and initialize request_number, which is
        #     going to be used as the brew batch id
        request_id = BrewRequest.get_request_id()
        brew_batch_id = ''

        # 2 - Get brew request number
        if request_id != '':
            brew_batch_id = BrewRequest.get_brew_request_number(request_id)
        else:
            main()
        # 3 - Update brew request
        BrewRequest.update_brew_stage(request_id, "Approval")

        # 4 - Get requested brew id based on request number
        item_id = BrewRequest.get_catalog_item_id(brew_batch_id)

        # 5 - Get requested item name based on its id
        item_name = BrewRequest.get_catalog_item_name(item_id)

        # 6 - Get recipe data and create a Python object based on brew request name
        recipe = BrewRequest.get_recipe(item_name)

        # 7 - Update brew request status
        BrewRequest.update_brew_stage(request_id, "Preparation Stage")

        # create order obj

        # create Prep BB Stage obj
        bb_stage = Brew.set_up_brew_stage(brew_batch_id)


        # Create Brew Batch Object

        # Hard-coded bb size value
        brew_batch = BrewBatch.BrewBatch(brew_batch_id, recipe, datetime.datetime.now(), bb_stage,
                                         "in prep",
                                         recipe.get_batch_size())

        # Call Prep
        s = Sanitization
        t = Temperature
        w = WeightScale
        q = QualityCheck_Prep
        s.Sanitization
        t.Temperature
        w.WeightScale
        q.QualityCheck
        Prep_Main.prep_main()
        # Call Mashing
        m = MillingMachine.MillingMachine()
        MillingMachine.MillingMachine.mill_grains(m, recipe)

        # Call Boiling
        boil_temp = recipe.get_boil_temp()
        boil_time = recipe.get_boil_time()
        Boil.run_boil(brew_batch_id, boil_temp, boil_time)

        # Call Ferment
        ferment_time = recipe.get_ferment_time()
        ferment_temp = recipe.get_ferment_temp()
        original_gravity = recipe.get_og()
        final_gravity = recipe.get_fg()
        recipe_abv = recipe.get_abv()
        Fermentation.start_fermentation_process(brew_batch_id)


        # Call Kegging
        recipe_ibu = recipe.get_ibu()
        kegging_process = KeggingMain(brew_batch_id, "BRITE_START,", recipe_ibu)
        kegging_process.start()

    except Exception as e:

        print("Error message: ", e)

    main()


if __name__ == "__main__":
    main()

