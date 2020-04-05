# Project: Brewing Automation System - Capstone Project
# Purpose Details: Kegging - Brewmaster Class
# Course: IST 440W - 001
# Author: Ronald Salguero
# Date Developed: 4/4/2020
# Last Date Changed:
# Rev: 1

class Brewmaster:
    def __init__(self, employee_id, employee_name, employee_role, active, rfid):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_role = employee_role
        self.active = active
        self.rfid = rfid

    def get_authorized_rfid(self):
        """
        This gets an authorized rfid number
        :return: rfid
        """
        return self.rfid

    def set_authorized_rfid(self):
        """
        This sets an authorized rfid number
        :return: rfid
        """
        return self.rfid