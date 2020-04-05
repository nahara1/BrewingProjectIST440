# Project: Brewing Automation System - Capstone Project
# Purpose Details: Kegging - Equipment Class
# Course: IST 440W - 001
# Author: Ronald Salguero
# Date Developed: 4/4/2020
# Last Date Changed:
# Rev: 1

"""

"""
class Equipment:
    def __init__(self, equipment_id, equipment_name, equipment_type, equipment_status, sanitation_status, connection_in, connection_out):
        self.equipment_id = equipment_id
        self.equipment_name = equipment_name
        self.equipment_type = equipment_type
        self.equipment_status = equipment_status
        self.sanitation_status = sanitation_status
        self.connection_in = connection_in
        self.connection_out = connection_out

    def get_equipment_id(self):
        """
        This gets the equipment ID
        :return: equipment_id
        """
        return self.equipment_id

    def set_equipment_id(self):
        """
        This sets the equipment ID
        :return: equipment_id
        """
        return self.equipment_id