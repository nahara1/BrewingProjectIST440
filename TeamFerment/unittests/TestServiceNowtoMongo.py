# Purpose Details: Unit test class for the ServiceNOW to Mongo class
# Course: IST 440
# Author: Team Ferment
# Date Developed: 4/1/2020
# Last Date Changed: 4/1/2020
# Rev: 1

import unittest
import requests
import json


class TestServiceNowtoMongo(unittest.TestCase):

    def test_get_recipe_body_json(self):
        url = 'https://emplkasperpsu2.service-now.com/api/now/table/x_snc_brewing440_recipe?sysparm_fields=sys_id' \
              '%2Crecipe_name%2Ctype%2Cstyle%2Cog%2Cfg%2Cabv%2Cibu%2Cwater_volume%2Cwater_temperature%2Cgrain_bill' \
              '%2Cboiling_duration%2Cyeast&sysparm_limit=100 '
        user = 'IST440'
        pwd = 'IST440'

        # Set proper headers
        headers = {"Content-Type": "application/json", "Accept": "application/json"}


if __name__ == '__main__':
    unittest.main()
