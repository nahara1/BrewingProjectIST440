# Project: Brewing Automation System - Capstone Project
# Purpose Details: Class to start brewing process
# Course: IST 440W - 001
# Author: IST 440W - 001
# Date Developed: 4/18/20
# Last Date Changed: 4/22/20
# Rev 22

import sys
from Brewing import Brew
from Brewing import BrewRequest
from Brewing import BrewBatch
from TeamFerment import Fermentation
from TeamPrep import Sanitization
from TeamPrep import Temperature
from TeamPrep import WeightScale
from TeamPrep import QualityCheck_Prep
from TeamMashing import MillingMachine
import datetime
from TeamBoiling import Boil
from TeamKegging.KeggingMain import KeggingMain
from TeamPrep.QualityCheck_Prep import QualityCheck
from Brewing import MongoLogging
from Brewing import ServiceNowLog


def call_prep(request_number, recipe):
    """
    Calls Team Prep's Process
    :param request_number: brew batch id
    :param recipe: a Recipe instance
    :return void
    """

    s = Sanitization.Sanitization()
    t = Temperature.Temperature()
    w = WeightScale.WeightScale()
    q = QualityCheck_Prep.QualityCheck()
    Sanitization.Sanitization.sanitization(s, request_number)
    Temperature.Temperature.yeast_temp(t, request_number)
    WeightScale.WeightScale.read_weight_grains(w, recipe, request_number)
    WeightScale.WeightScale.read_weight_hops(w, recipe, request_number)
    while not QualityCheck_Prep.QualityCheck.get_QA_Check(q, request_number):
        print("Prep QA Failed")

    return True


def call_mash(request_number, recipe):
    """
    Calls Team Mashing's Process
    :param request_number: brew batch id
    :param recipe: a Recipe instance
    :return: void
    """
    m = MillingMachine.MillingMachine()
    MillingMachine.MillingMachine.mill_grains(m, recipe, request_number)
    return True


def call_boil(request_number, recipe):
    """
    Calls Team Boil's Process
    :param request_number: brew batch id
    :param recipe: a Recipe instance
    :return: void
    """
    boil_temp = recipe.get_boil_temp()
    boil_time = recipe.get_boil_time()
    return Boil.run_boil(request_number, boil_temp, boil_time)


def call_ferment(request_number, recipe):
    """
    Method Calls Team Ferment's Process
    :param request_number: brew batch id
    :param recipe: a Recipe Instance
    :return: void
    """
    Fermentation.start_fermentation_process(request_number, recipe)
    return True


def call_kegging(request_number, recipe):
    """
    Method Calls Team Kegging's Process
    :param request_number: brew batch id
    :param recipe: a Recipe Instance
    :return: void
    """
    recipe_ibu = recipe.get_ibu()
    kegging_process = KeggingMain(request_number, "BRITE_START,", recipe_ibu)
    kegging_process.start()
    return True


def brew_loops(request_number, request_id, recipe):
    """
    Initiates each brewing stage under the condition that the preceding one has been
    successfully completed. Otherwise, the preparation stage method is called again in
    order for a new attempt to be made.

    :param request_number: brew batch id
    :param request_id: order request id
    :param recipe: a Recipe Instance
    :return: void
    """
    try:
        prep_pass = False

        while not prep_pass:
            # Call Prep
            if call_prep(request_number, recipe):

                # Update Request Stage
                BrewRequest.update_brew_stage(request_id, "Mashing Stage")
                prep_pass = True

            else:
                print("Prep Stage not completed.")
                print("Making new batch attempt...")

            mash_pass = False

            while not mash_pass and prep_pass:
                # Call Mashing
                if call_mash(request_number, recipe):
                    # Update Request Stage
                    BrewRequest.update_brew_stage(request_id, "Boiling Stage")
                    mash_pass = True

                else:
                    print("Mash Stage not completed.")
                    print("Making new batch attempt...")
                    prep_pass = False
                    break

            boil_pass = False

            while not boil_pass and prep_pass:
                # Call Boil
                if call_boil(request_number, recipe):
                    # Update Request Stage
                    BrewRequest.update_brew_stage(request_id, "Fermentation Stage")
                    boil_pass = True

                else:
                    print("Boil Stage not completed.")
                    print("Making new batch attempt...")
                    prep_pass = False
                    break

            ferment_pass = False

            while not ferment_pass and prep_pass:
                # Call Ferment
                if call_ferment(request_number, recipe):
                    # Update Request Stage
                    BrewRequest.update_brew_stage(request_id, "Kegging Stage")
                    ferment_pass = True

                else:
                    print("Ferment Stage not completed.")
                    print("Making new batch attempt...")
                    prep_pass = False
                    break

            kegging_pass = False

            while not kegging_pass and prep_pass:
                # Call Kegging
                if call_kegging(request_number, recipe):
                    print("Batch is completed")
                    BrewRequest.update_brew_stage(request_id, "All Stages Completed")
                    BrewRequest.update_brew_stage(request_id, "Complete")
                    kegging_pass = True
                else:
                    print("Kegging Stage not completed.")
                    print("Making new batch attempt...")
                    prep_pass = False
                    break

    except Exception as e:

        print("Error message: ", e)


def main():
    """
    Gets brew requests from ServiceNow and initiates brewing through its completion
    :return: void
    """
    print("-----------------------------------------\n")
    print("       Welcome to Balrog Brewery\n")
    print("-----------------------------------------\n")

    input("Press any key to continue: \n")
    print("Fetching brew request...\n")

    # Get a brew request
    # 1 - Get brew request id and initialize request_number, which is
    #     going to be used as the brew batch id
    request_id = BrewRequest.get_request_id()
    print("Request ID: ", request_id)
    request_number = ''

    # 2 - Get brew request number
    if request_id != '':
        request_number = BrewRequest.get_brew_request_number(request_id)
    else:
        main()
    # 3 - Update brew request
    BrewRequest.update_brew_stage(request_id, "Requested")
    BrewRequest.update_brew_stage(request_id, "Approval")


    # 4 - Get requested brew id based on request number
    item_id = BrewRequest.get_catalog_item_id(request_number)

    # 5 - Get requested item name based on its id
    item_name = BrewRequest.get_catalog_item_name(item_id)

    # 6 - Get recipe data and create a Python object based on brew request name
    recipe = BrewRequest.get_recipe(item_name)

    # 7 - Update brew request status
    BrewRequest.update_brew_stage(request_id, "Preparation Stage")

    # Create Prep BB Stage obj
    bb_stage = Brew.set_up_brew_stage(request_number)

    # Create Brew Batch Object
    brew_batch = BrewBatch.BrewBatch(request_number, recipe, datetime.datetime.now(), bb_stage,
                                     "in prep",
                                     recipe.get_batch_size())

    # brew_loops(request_number, request_id, recipe)
    brew_loops(request_number, request_id, recipe)

    # single process call testings

    main()


if __name__ == "__main__":
    main()
