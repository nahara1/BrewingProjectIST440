# Project: Brewing Project
# Purpose Details: Taster Class
# Course: IST 440W
# Author: Team Kegging - Jun Baek
# Date Developed: 4/5/2020
# Last Date Changed: 4/5/2020
# Rev: 1.0


class TasterClass:  #Taster Class
    def __init__(self, tc_id, tc_name, tc_role):
        self.tc_id = tc_id
        self.tc_name = tc_name
        self.tc_role = tc_role

    def get_status(self):
        return "Taster_ID: {}\n" \
               "Taster_Name: {}\n" \
               "Taster_Role: {}\n".format(self.tc_id, self.tc_name, self.tc_role)

testTaster = TasterClass(12, "Jun Baek", "Quality Assurance 1")

print(testTaster.get_status())