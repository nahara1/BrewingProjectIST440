# Project: Brewing Automation System - Capstone Project
# Purpose Details: Class to start brewing process
# Course: IST 440W - 001
# Author: IST 440W - 001
# Date Developed: 4/18/20
# Last Date Changed: 4/22/20
# Rev 22
from typing import Type, Union

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
    :return none
    """

    s = Sanitization.Sanitization()
    t = Temperature.Temperature()
    w = WeightScale.WeightScale()
    q = QualityCheck_Prep.QualityCheck()
    Sanitization.Sanitization.sanitization(s, request_number)
    Temperature.Temperature.yeast_temp(t, request_number)
    WeightScale.WeightScale.read_weight_grains(w, recipe, request_number)
    WeightScale.WeightScale.read_weight_hops(w, recipe,request_number)
    QualityCheck_Prep.QualityCheck.get_QA_Check(q, request_number)

def call_mash(request_number, recipe):
    """
    Calls Team Mashing's Process
    :param request_number: brew batch id
    :param recipe: a Recipe instance
    :return: none
    """
    m = MillingMachine.MillingMachine()
    MillingMachine.MillingMachine.mill_grains(m, recipe, request_number)


def call_boil(request_number, recipe):
    """
    Calls Team Boil's Process
    :param request_number: brew batch id
    :param recipe: a Recipe instance
    :return: none
    """
    boil_temp = recipe.get_boil_temp()
    boil_time = recipe.get_boil_time()
    Boil.run_boil(request_number, boil_temp, boil_time)


def call_ferment(request_number, recipe):
    """
    Method Calls Team Ferment's Process
    :param request_number:
    :param recipe:
    :return: none
    """
    Fermentation.start_fermentation_process(request_number, recipe)


def call_kegging(request_number, recipe):
    """
    Method Calls Team Kegging's Process
    :param request_number:
    :param recipe:
    :return:
    """
    recipe_ibu = recipe.get_ibu()
    kegging_process = KeggingMain(request_number, "BRITE_START,", recipe_ibu)
    kegging_process.start()


def main():
    """
    Gets brew requests from ServiceNow and initiates brewing through its completion
    :return: none
    """

    # Get a brew request
    # 1 - Get brew request id and initialize request_number, which is
    #     going to be used as the brew batch id
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

    # Create Prep BB Stage obj
    bb_stage = Brew.set_up_brew_stage(request_number)

    # Create Brew Batch Object
    brew_batch = BrewBatch.BrewBatch(request_number, recipe, datetime.datetime.now(), bb_stage,
                                     "in prep",
                                     recipe.get_batch_size())

    try:

        # Call Prep
        #call_prep(request_number, recipe)

        # Update Request Stage
        BrewRequest.update_brew_stage(request_id, "Mashing Stage")

        # Call Mashing
        call_mash(request_number, recipe)

        # Update Request Stage
        BrewRequest.update_brew_stage(request_id, "Boiling Stage")

        # Call Boil
        call_boil(request_number, recipe)

        # Update Request Stage
        BrewRequest.update_brew_stage(request_id, "Fermentation Stage")

        # Call Ferment
        call_ferment(request_number, recipe)

        # Update Request Stage
        BrewRequest.update_brew_stage(request_id, "Kegging Stage")

        # Call Kegging
        # call_kegging(request_number, recipe)

    except Exception as e:

        print("Error message: ", e)

    main()


if __name__ == "__main__":
    main()
#This is a test of github at 9:33 on 4/23/2020