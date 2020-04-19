
from Brewing import Recipe
from Brewing import Brew
from Brewing import BrewRequest
from Brewing import BrewBatch
from TeamPrep import  Sanitization
from TeamPrep import Temperature
from TeamPrep import WeightScale
from TeamPrep import QualityCheck_Prep
from TeamPrep import Prep_Main
from Brewing import BrewBatchStage
from TeamMashing import MillingMachine
import datetime
from TeamBoiling import Boil
from TeamKegging.KeggingMain import KeggingMain
from Brewing import Log
import sys
import time
import threading


def main():
    # Get a brew request

    try:
        # 1 - Get brew request id and initialize request_number
        request_id = BrewRequest.get_request_id()
        request_number = ''

        # 2 - Get brew request number
        if request_id != '':
            request_number = BrewRequest.get_brew_request_number(request_id)
        else:
            main()
        # 3 - Update brew request
        BrewRequest.update_brew_stage(request_id, "Approval")

        # 4 - Get requested brew id based on request number
        item_id = BrewRequest.get_catalog_item_id(request_number)

        # 5 - Get requested item name based on its id
        item_name = BrewRequest.get_catalog_item_name(item_id)

        # 6 - Get recipe data and create a Python object based on brew request name
        recipe = BrewRequest.get_recipe(item_name)

        # 7 - Update brew request status
        BrewRequest.update_brew_stage(request_id, "Preparation Stage")

        # create order obj

        # create Prep BB Stage obj
        bb_stage = Brew.set_up_brew_stage(request_number)


        # Create Brew Batch Object

        # Hard-coded bb size value
        brew_batch = BrewBatch.BrewBatch(request_number, recipe, datetime.datetime.now(), bb_stage,
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
        Prep.Prep_Main(s,t, w,q)
        # Call Mashing
        m = MillingMachine.MillingMachine()
        MillingMachine.MillingMachine.mill_grains(m, recipe)

        # Call Boiling
        boil_temp = recipe.get_boil_temp()
        boil_time = recipe.get_boil_time()
        Boil.run_boil(request_number, boil_temp, boil_time)

        # Call Ferment


        # Call Kegging
        recipe_ibu = recipe.get_ibu()
        kegging_process = KeggingMain.KeggingMain(request_id, "BRITE_START,", recipe_ibu)
        kegging_process.start()
    except Exception as e:

        print("Error message: ", e)

    main()


if __name__ == "__main__":
    main()

