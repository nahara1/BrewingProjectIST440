# Project: Brewing Automation System - Capstone Project
# Purpose Details: Class for the Customer data
# Course: IST 440W - 001
# Author: TeamPrep
# Date Developed: Development Phase
# Last Date Changed: 4/8/2020
class Customer:
    def __init__(self, customer_id, customer_name, customer_address, customer_phone, customer_email):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_address = customer_phone
        self.customer_address = customer_email
        customer_id = int
        customer_name = str
        customer_address = str
        customer_phone = int
        customer_email = str

    def get_customer_id(self):
        '''
        gets the customer id
        :return: customer id
        '''
        return self.customer_id

    def get_customer_name(self):
        '''
        gets the customer name
        :return: customer name
        '''
        return self.customer_name

    def get_customer_address(self):
        '''
        gets the customer address
        :return: customer address
        '''
        return self.employee_address

    def get_customer_phone(self):
        '''
        gets the customer phone number
        :return: customer phone number
        '''
        return self.employee_phone

    def get_customer_email(self):
        '''
        gets the customer email
        :return: customer email
        '''
        return self.employee_email
