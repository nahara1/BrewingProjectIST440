# Project: Brewing Automation System - Capstone Project
# Purpose Details: Kegging - Equipment Class
# Course: IST 440W - 001
# Author: Ronald Salguero
# Date Developed: 4/4/2020
# Last Date Changed:
# Rev: 1

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

    def get_equipment_name(self):
        """
        This gets the equipment name
        :return: equipment_name
        """
        return self.equipment_name

    def set_equipment_name(self):
        """
        This sets the equipment name
        :return: equipment_name
        """
        return self.equipment_name

    def get_equipment_type(self):
        """
        This gets the equipment type
        :return: equipment_type
        """
        return self.equipment_type

    def set_equipment_type(self):
        """
        This sets the equipment type
        :return: equipment_type
        """
        return self.equipment_type

    def get_equipment_status(self):
        """
        This gets the equipment status
        :return: equipment_status
        """
        return self.equipment_status

    def set_equipment_status(self):
        """
        This sets the equipment status
        :return: equipment_status
        """
        return self.equipment_status

    def update_equipment_status(self):
        """
        This updates the equipment status
        :return: equipment_status
        """
        return self.equipment_status

    def get_sanitation_status(self):
        """
        This gets the sanitation status
        :return: sanitation_status
        """
        return self.sanitation_status

    def set_sanitation_status(self):
        """
        This sets the sanitation status
        :return: sanitation_status
        """
        return self.sanitation_status

    def update_sanitation_status(self):
        """
        This updates the equipment status
        :return: sanitation_status
        """
        return self.sanitation_status

    def get_connection_in(self):
        """
        This gets the connection in
        :return: connection_in
        """
        return self.connection_in

    def set_connection_in(self):
        """
        This sets the connection in
        :return: connection_in
        """
        return self.connection_in

    def get_connection_out(self):
        """
        This gets the connection out
        :return: connection_out
        """
        return self.connection_out

    def set_connection_out(self):
        """
        This sets the connection out
        :return: connection_out
        """
        return self.connection_out