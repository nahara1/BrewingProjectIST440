# Project: Brewing Automation System - Capstone Project
# Purpose Details: Kegging - Keg Class
# Course: IST 440W - 001
# Author: Ronald Salguero
# Date Developed: 4/4/2020
# Last Date Changed: 4/18/2020
# Rev: 1.1

class Keg:
    def __init__(self, keg_id, keg_style, current_volume, keg_pressure, max_volume):
        self.keg_id = keg_id
        self.keg_style = keg_style
        self.current_volume = current_volume
        self.keg_pressure = keg_pressure
        self.max_volume = max_volume

    def get_status(self):
        """
        Gets the status of the keg object

        :return: Keg object
        """
        try:
            return "Keg ID: {}\n" \
                   "Keg Type: {}\n" \
                   "Keg Current Volume: {}\n" \
                   "Keg Pressure: {}\n" \
                   "Keg Max Volume: {}\n".format(self.keg_id, self.keg_style, self.current_volume, self.keg_pressure,
                                                 self.max_volume)
        except Exception as e:
            print("Error Message: " + e)

    def get_info(self):
        '''
        Gets the information of keg object, formatted to be logged into ServiceNow

        :return: Keg object
        '''
        try:
            return "Keg ID: {} :: " \
                   "Keg Type: {} :: " \
                   "Keg Current Volume: {} :: " \
                   "Keg Pressure: {} :: " \
                   "Keg Max Volume: {} :: ".format(self.keg_id, self.keg_style, self.current_volume, self.keg_pressure,
                                                   self.max_volume)
        except Exception as e:
            print("Error Message: " + e)

    def set_style_sixtel(self):
        """
        Function that is used to set the keg container to a sixtel container

        :param max_volume : the maximum volume that a keg can hold to be labeled as a sixtel
        :param keg_style : the style of the keg being used
        :return: float
        """
        self.max_volume = 5.16
        self.keg_style = "KEG_SIXTEL"

    def set_style_quarter_stubby(self):
        '''
        Function that is used to set the keg container to a quarter stubby container

        :param max_volume : the maximum volume that a keg can hold to be labeled as a quarter stubby
        :param keg_style : the style of the keg being used
        :return: float
        '''
        self.max_volume = 7.75
        self.keg_style = "KEG_QUARTER_STUBBY"

    def set_style_quarter_slim(self):
        '''
        Function that is used to set the keg container to a quarter slim container

        :param max_volume : the maximum volume that a keg can hold to be labeled as a quarter slim
        :param keg_style : the style of the keg being used
        :return: float
        '''
        self.max_volume = 7.75
        self.keg_style = "KEG_QUARTER_SLIM"
