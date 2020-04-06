# Project: Brewing Project
# Purpose Details: Cellarman Class
# Course: IST 440W
# Author: Team Kegging - Jun Baek
# Date Developed: 4/5/2020
# Last Date Changed: 4/5/2020
# Rev: 1.0


class CellarmanClass:  #Cellarman Class
    def __init__(self, cc_id, cc_name, cc_role):
        self.cc_id = cc_id
        self.cc_name = cc_name
        self.cc_role = cc_role

    def get_status(self):
        return "Cellarman_ID: {}\n" \
               "Cellarman_Name: {}\n" \
               "Cellarman_Role: {}\n".format(self.cc_id, self.cc_name, self.cc_role)

testCellarman = CellarmanClass(12, "Jun Baek", "Quality Assurance 1")

print(testCellarman.get_status())