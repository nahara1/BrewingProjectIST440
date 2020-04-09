# Project: Brewing Automation System - Capstone Project
# Purpose Details:
# Course: IST 440W - 001
# Author: Antonio Rivera :)
# Date Developed:
# Last Date Changed:
# Rev
class Order:
    def __init__(self, order_id, order_date, order_status):
        self.order_id = order_id
        self.order_date = order_date
        self.order_status = order_status

    def get_order_id(self):
        '''
        gets the order id
        :return: order id
        '''
        return self.order_id

    def get_order_date(self):
        '''
        gets the order date
        :return: order date
        '''
        return self.order_date

    def get_order_status(self):
        '''
        gets the order status
        :return: order status
        '''
        return self.order_status
