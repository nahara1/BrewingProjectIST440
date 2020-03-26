# Team Boiling
# 3/17/2020
# Created by Erik Ellis, eae5206@psu.edu


class DisplayHelper():

    def __init__(self):
        _lcd_display = object
        _led_matrix = object

    def get_lcd_display_data(self):
        return self._lcd_display

    def set_lcd_display(self, display):
        self.lcd_display = display

    def get_led_matrix_data(self):
        return self._led_matrix

    def set_led_matrix(self, matrix):
        self._led_matrix = matrix

    def send_data(self, display, matrix):
        display, matrix
