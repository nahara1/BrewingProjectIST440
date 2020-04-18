# Project: Brewing Project
# Purpose Details: Brite Tank Object
# Course: IST 440W
# Author: Team Kegging - Daibo Zhang
# Date Developed: 4/03/2020
# Last Date Changed: 4/15/2020
# Rev: 1.3

import math
import time
import datetime
from Brewing.Recipe import Recipe
from Brewing import ServiceNowLog

sim_sleep_mod = .05 # Contains the simulated delay in seconds for automatic Temperature and Pressure Controls
bt_loglist = []

class KeggingBriteTank:  #Brite Tank
    def __init__(self, bt_id, bt_temp, bt_max_volume, bt_current_volume, bt_psi, bt_status):
        self.bt_id = bt_id
        self.bt_temp = bt_temp
        self.bt_max_volume = bt_max_volume
        self.bt_current_volume = bt_current_volume
        self.bt_psi = bt_psi
        self.bt_status = bt_status

    def get_status(self):
        """
        Basic return string status method, use print_carb_status() for carbonation status instead.
        :return: Brite Tank Status
        """
        return "Brite Tank ID: {}\n" \
               "Brite Tank Temperature: {}\n" \
               "Brite Tank Max_Volume: {}\n" \
               "Brite Tank Volume: {}\n" \
               "Brite Tank PSI: {}\n" \
               "Brite Tank Status: {}\n".format(self.bt_id, self.bt_temp, self.bt_max_volume, self.bt_current_volume, self.bt_psi, self.bt_status)

    def get_carbonation(self):
        """
        Returns the Carbonation level of the Brita Tank based off of Temperature and Pressure. Min Temp is 30F, Max Temp is 65F. Min PSI is 1, Max PSI is 30.
        :return: Carbonation vols if Temp and PSI are within range, else returns Unknown as a string
        """
        carbchart = [["Carbchart"],\
        [30,1.82,1.92,2.03,2.14,2.23,2.36,2.48,2.6,2.7,2.82,2.93,3.02,3.13,3.24,3.35,3.46,3.57,3.67,3.78,3.89,4,4.11,4.22,4.33,4.44,4.66,4.77,4.87,4.98,4.98],\
        [31,1.78,1.88,2,2.1,2.2,2.31,2.42,2.54,2.65,2.76,2.86,2.96,3.07,3.17,3.28,3.39,3.5,3.6,3.71,3.82,3.93,4.03,4.14,4.25,4.35,4.46,4.57,4.68,4.78,4.89],\
        [32,1.75,1.85,1.95,2.05,2.15,2.27,2.38,2.48,2.59,2.7,2.8,2.9,3,3.11,3.21,3.31,3.42,3.52,3.63,3.73,3.84,3.94,4.04,4.15,4.25,4.36,4.46,4.57,4.67,4.77],\
        [33,1.71,1.81,1.91,2.01,2.1,2.23,2.33,2.43,2.53,2.63,2.74,2.84,2.96,3.06,3.15,3.25,3.35,3.46,3.56,3.66,3.76,3.87,3.97,4.07,4.18,4.28,4.38,4.48,4.59,4.69],\
        [34,1.68,1.78,1.86,1.97,2.06,2.18,2.28,2.38,2.48,2.58,2.69,2.79,2.90,3.00,3.09,3.19,3.29,3.39,3.49,3.59,3.69,3.79,3.90,4.00,4.1,4.2,4.3,4.4,4.5,4.60],\
        [35,1.63,1.73,1.83,1.93,2.02,2.14,2.24,2.34,2.43,2.52,2.63,2.73,2.83,2.93,3.02,3.12,3.22,3.32,3.42,3.52,3.62,3.72,3.82,3.92,4.01,4.11,4.21,4.31,4.41,4.51],\
        [36,1.6,1.69,1.79,1.88,1.98,2.09,2.19,2.29,2.38,2.47,2.57,2.67,2.77,2.86,2.96,3.05,3.15,3.24,3.34,3.43,3.53,3.63,3.72,3.82,3.92,4.01,4.11,4.21,4.3,4.4],\
        [37,1.55,1.65,1.74,1.84,1.94,2.04,2.14,2.24,2.33,2.42,2.52,2.62,2.71,2.8,2.9,3,3.09,3.18,3.27,3.37,3.46,3.56,3.65,3.75,3.84,3.94,4.03,4.13,4.22,4.32],\
        [38,1.52,1.61,1.71,1.8,1.9,2,2.1,2.2,2.29,2.38,2.48,2.57,2.66,2.75,2.85,2.94,3.03,3.12,3.21,3.3,3.4,3.49,3.59,3.68,3.77,3.87,3.96,4.06,4.15,4.24],\
        [39,1.49,1.58,1.67,1.77,1.86,1.96,2.06,2.15,2.25,2.34,2.43,2.52,2.61,2.7,2.8,2.89,2.98,3.07,3.16,3.25,3.34,3.44,3.53,3.62,3.71,3.81,3.9,3.99,4.08,4.18],\
        [40,1.47,1.56,1.65,1.74,1.83,1.92,2.01,2.1,2.2,2.3,2.39,2.47,2.56,2.65,2.75,2.84,2.93,3.01,3.1,3.19,3.28,3.37,3.46,3.55,3.64,3.73,3.82,3.91,4.01,4.1],\
        [41,1.43,1.52,1.61,1.7,1.79,1.88,1.97,2.06,2.16,2.25,2.34,2.43,2.52,2.6,2.7,2.79,2.88,2.96,3.05,3.14,3.23,3.32,3.41,3.5,3.59,3.68,3.77,3.86,3.95,4.04],\
        [42,1.39,1.48,1.57,1.66,1.75,1.85,1.94,2.02,2.12,2.21,2.3,2.39,2.48,2.56,2.65,2.74,2.83,2.91,3,3.09,3.18,3.26,3.35,3.44,3.53,3.62,3.7,3.79,3.88,3.97],\
        [43,1.37,1.46,1.54,1.63,1.72,1.81,1.9,1.99,2.08,2.17,2.26,2.34,2.43,2.52,2.61,2.69,2.78,2.86,2.95,3.04,3.13,3.21,3.3,3.39,3.47,3.56,3.65,3.74,3.82,3.91],\
        [44,1.35,1.43,1.52,1.6,1.69,1.78,1.87,1.95,2.04,2.13,2.22,2.3,2.39,2.47,2.56,2.64,2.73,2.81,2.9,2.99,3.07,3.1,3.24,3.33,3.41,3.5,3.58,3.67,3.76,3.84],\
        [45,1.32,1.41,1.49,1.58,1.66,1.75,1.84,1.91,2,2.08,2.17,2.26,2.34,2.42,2.51,2.6,2.69,2.77,2.86,2.94,3.02,3.11,3.19,3.28,3.36,3.45,3.53,3.62,3.7,3.79],\
        [46,1.28,1.37,1.45,1.54,1.62,1.71,1.8,1.88,1.96,2.04,2.13,2.22,2.3,2.38,2.47,2.55,2.64,2.72,2.81,2.89,2.98,3.06,3.15,3.23,3.31,3.4,3.48,3.57,3.65,3.74],\
        [47,1.26,1.34,1.42,1.51,1.59,1.68,1.76,1.84,1.92,2,2.09,2.18,2.26,2.34,2.42,2.5,2.59,2.67,2.76,2.84,2.93,3.02,3.09,3.18,3.26,3.35,3.43,3.51,3.6,3.68],\
        [48,1.23,1.31,1.39,1.48,1.56,1.65,1.73,1.81,1.89,1.96,2.05,2.14,2.22,2.3,2.38,2.46,2.54,2.62,2.71,2.79,2.88,2.96,3.04,3.13,3.21,3.3,3.38,3.46,3.54,3.63],\
        [49,1.21,1.29,1.37,1.45,1.53,1.62,1.7,1.79,1.86,1.93,2.01,2.1,2.18,2.25,2.34,2.42,2.5,2.58,2.67,2.75,2.83,2.91,3,3.07,3.15,3.23,3.31,3.39,3.47,3.56],\
        [50,1.18,1.26,1.34,1.42,1.5,1.59,1.66,1.74,1.82,1.9,1.98,2.06,2.14,2.21,2.3,2.38,2.46,2.54,2.62,2.7,2.78,2.86,2.94,3.02,3.1,3.17,3.25,3.33,3.41,3.49],\
        [51,1.18,1.26,1.34,1.42,1.49,1.57,1.64,1.71,1.79,1.87,1.95,2.02,2.1,2.18,2.26,2.34,2.42,2.49,2.57,2.65,2.74,2.82,2.9,2.97,3.05,3.13,3.19,3.27,3.34,3.42],\
        [52,1.16,1.23,1.31,1.39,1.46,1.54,1.61,1.68,1.76,1.84,1.92,1.99,2.06,2.14,2.22,2.3,2.38,2.45,2.53,2.61,2.68,2.76,2.84,2.92,3,3.06,3.13,3.22,3.3,3.37],\
        [53,1.14,1.21,1.29,1.36,1.44,1.51,1.59,1.66,1.74,1.81,1.89,1.96,2.03,2.1,2.18,2.26,2.34,2.41,2.49,2.57,2.64,2.71,2.79,2.86,2.94,3.01,3.09,3.16,3.24,3.31],\
        [54,1.12,1.19,1.27,1.34,1.41,1.49,1.56,1.63,1.71,1.78,1.86,1.93,2,2.07,2.15,2.22,2.3,2.37,2.45,2.52,2.59,2.66,2.74,2.81,2.89,2.96,3.04,3.1,3.17,3.24],\
        [55,1.1,1.17,1.24,1.31,1.39,1.46,1.53,1.6,1.68,1.75,1.82,1.89,1.97,2.04,2.12,2.18,2.26,2.33,2.4,2.47,2.54,2.62,2.69,2.76,2.83,2.89,2.97,3.04,3.11,3.18],\
        [56,1.07,1.15,1.22,1.29,1.36,1.43,1.5,1.57,1.65,1.72,1.79,1.86,1.93,2,2.08,2.15,2.22,2.29,2.36,2.43,2.5,2.57,2.64,2.71,2.78,2.85,2.92,2.99,3.06,3.13],\
        [57,1.05,1.12,1.19,1.26,1.33,1.4,1.47,1.54,1.62,1.7,1.77,1.83,1.9,1.97,2.04,2.11,2.18,2.25,2.32,2.39,2.46,2.53,2.6,2.66,2.73,2.8,2.87,2.94,3,3.08],\
        [58,1.03,1.1,1.17,1.24,1.3,1.37,1.44,1.51,1.59,1.67,1.74,1.8,1.87,1.94,2.01,2.08,2.15,2.21,2.28,2.35,2.42,2.48,2.55,2.62,2.69,2.75,2.82,2.88,2.95,3.02],\
        [59,1.02,1.09,1.16,1.22,1.29,1.36,1.43,1.49,1.56,1.64,1.71,1.77,1.84,1.91,1.98,2.04,2.11,2.17,2.24,2.31,2.38,2.43,2.5,2.57,2.64,2.7,2.77,2.84,2.91,2.97],\
        [60,1.01,1.08,1.15,1.21,1.28,1.34,1.41,1.47,1.54,1.62,1.62,1.75,1.82,1.88,1.95,2.01,2.08,2.14,2.21,2.27,2.34,2.4,2.47,2.53,2.6,2.66,2.73,2.79,2.86,2.92],\
        [61,0.99,1.05,1.12,1.18,1.24,1.31,1.37,1.44,1.5,1.57,1.63,1.69,1.76,1.82,1.89,1.95,2.02,2.08,2.14,2.21,2.27,2.34,2.4,2.47,2.53,2.59,2.66,2.72,2.79,2.85],\
        [62,0.96,1.02,1.09,1.15,1.21,1.27,1.34,1.4,1.46,1.52,1.59,1.65,1.71,1.78,1.84,1.9,1.97,2.03,2.09,2.15,2.22,2.28,2.34,2.41,2.47,2.53,2.59,2.66,2.72,2.78],\
        [63,0.93,0.99,1.06,1.12,1.18,1.24,1.3,1.36,1.42,1.49,1.55,1.61,1.67,1.73,1.79,1.85,1.92,1.98,2.04,2.1,2.16,2.22,2.28,2.35,2.41,2.47,2.53,2.59,2.65,2.71],\
        [64,0.91,0.97,1.03,1.09,1.15,1.21,1.27,1.33,1.39,1.45,1.51,1.57,1.63,1.69,1.75,1.81,1.87,1.93,1.99,2.05,2.11,2.17,2.23,2.29,2.35,2.41,2.47,2.52,2.58,2.64],\
        [65,0.88,0.94,1,1.06,1.11,1.17,1.23,1.29,1.35,1.41,1.46,1.52,1.58,1.64,1.7,1.76,1.82,1.87,1.93,1.99,2.05,2.11,2.17,2.23,2.28,2.34,2.4,2.46,2.52,2.58]]

        carbcharttemp = math.floor(self.bt_temp) - 29
        carbchartpsi = math.floor(self.bt_psi)
        batchcarb = carbchart[carbcharttemp][carbchartpsi]

        if 30 <= self.bt_temp <= 65 and 1 <= self.bt_psi < 31:
            return batchcarb
        elif self.bt_temp < 30 or self.bt_temp >= 30:
            return "Unknown"
        elif self.bt_psi < 1 or self.bt_psi >= 31:
            return "Unknown"
        else:
            return "Error"

    def get_volume_dif(self):
        """
        Gets the volume difference for the brite tank
        :param bt_current_volume
        :param bt_max_volume
        :return: Remaining free volume of the brite tank
        """
        if self.bt_current_volume < self.bt_max_volume:
            return self.bt_max_volume - self.bt_current_volume

    def update_bt_temp(self, cur_temp):
        """
        Updates the brite tank object with the temperature and returns the value
        :param cur_temp: the current tank temperature
        :return: Current Temperature of the Brite Tank
        """
        self.bt_temp = cur_temp
        return cur_temp

    def get_bt_temp(self):
        """
        Gets the current tank temperature in Fahrenheit and returns the value
        :return: Tank Temperature
        """
        return self.bt_temp

    def update_bt_psi(self, cur_psi):
        """
        Updates the tank pressure and returns the value
        :param cur_psi: the current tank pressure
        :return: Current PSI of the Brite Tank
        """
        self.bt_psi = cur_psi
        return cur_psi

    def get_bt_psi(self):
        """
        Gets the current tank pressure in PSI and returns the value
        :return: Current Tank Pressure
        """
        return self.bt_psi

    def print_carb_status(self):
        """
        Prints the Temperature, Pressure, and Carbonation Status of the brite tank.

        :return: Brite Tank status text
        """
        print("Tank Temperature: " + str(self.bt_temp) + " degrees Fahrenheit || Tank Pressure: " + str(self.bt_psi)+ " PSI || Carbonation: " + str(self.get_carbonation()) +" vols")

    def bt_temp_control(self):
        """
        Main temperature for checking whether the temperature of the brite tank is in detectable range.

        :return: Sets the brite tank temperature and status as BT_TEMPERATURE_READY
        """
        try:
            print("")
            if self.bt_temp < 30:
                print("Tank temperature is less than 30 degrees Fahrenheit. Please raise tank temperature above 30 degrees Fahrenheit.")
                self.temp_choice()
            elif self.bt_temp >= 66:
                print("Tank temperature is greater than 66 degrees Fahrenheit. Please lower tank temperature below 66 degrees Fahrenheit.")
                self.temp_choice()
            elif 33 <= self.bt_temp < 66:
                print("The tank temperature is in detectable range but not between the ideal range of 30 to 32 degrees Fahrenheit.")
                self.temp_choice()
            elif 30 <= self.bt_temp < 33:
                print("The tank temperature in in the ideal range.")
                self.bt_status = "BT_TEMPERATURE_READY"
        except Exception as e:
            print(e)



    def temp_choice(self):
        """
        Method that allows a user to chose between manual or automatic operation of temperature controls. Only allows temperature to be set between 30 and 65 degrees Fahrenheit

        :return: Sets the bright tank temperature between 30 and 65 degrees Fahrenheit
        """
        selection = False
        while not selection:
            choice = input("Would you like to Manually or Automatically Adjust Temperature? Enter (M/A) or (N) to exit: ")
            if choice in ['m', 'M', 'manual', 'Manual', 'MANUAL', 'manually', 'Manually', 'MANUALLY']:
                selection = True
                temp_ready = False
                while not temp_ready:
                    print("You have selected Manual temperature operation.")
                    new_temp = float(input("When the brite tank has reached your desired temperature, enter its value (degrees Fahrenheit): "))
                    if 30 <= new_temp < 66:
                        temp_ready = True
                        self.update_bt_temp(new_temp)
                    else:
                        print("")
                        print("Please adjust the temperature between 30 and 65 degrees Fahrenheit.")
                self.print_carb_status()
            elif choice in ['a', 'A', 'auto', 'Auto', 'AUTO', 'automatically', 'Automatically', 'AUTOMATICALLY']:
                selection = True
                temp_ready = False
                while not temp_ready:
                    print("You have selected Automatic temperature operation.")
                    target_temp = float(input("Enter the target Temperature (degrees Fahrenheit): "))
                    if 30 <= target_temp < 66:
                        temp_ready = True
                        self.auto_temp(target_temp) # contains the simulated delay value for temperature adjustments for temperature values
                    else:
                        print("")
                        print("Please enter a temperature between 30 and 65 degrees Fahrenheit.")
            elif choice in ['N','n','no','No','NO']:
                selection = True

    def auto_temp(self, target_temp):
        """
        Method that simulates automatic temperature adjustment through a delay.

        :param target_temp: The target temperature of the brite tank in degrees Fahrenheit
        :return: Sets the temperature in the brite tank to the specified degree Fahrenheit
        """
        while self.bt_temp != target_temp:
            time.sleep(sim_sleep_mod)
            if self.bt_temp < target_temp and abs(self.bt_temp -target_temp) >= 1:
                self.bt_temp += 1
            elif self.bt_temp > target_temp and abs(self.bt_temp -target_temp) >= 1:
                self.bt_temp -= 1
            elif abs(self.bt_temp - target_temp) < 1 or self.bt_temp == target_temp:
                self.bt_temp = target_temp
            else:
                print("Error")
            self.print_carb_status()
        return self.bt_temp

    def bt_psi_control(self):
        """
        Main brite tank pressure control to see if pressure is within detectable range.

        :return: sets the brite tank PSI and status to BT_PSI_READY
        """
        try:
            print("")
            if self.bt_psi < 1:
                print("Tank pressure is less than 1 PSI. Please raise tank pressure above 1 PSI.")
                self.psi_choice()
            elif self.bt_temp >= 31:
                print("Tank pressure is greater than 31 PSI. Please lower tank pressure below 31 PSI.")
                self.psi_choice()
            elif 1 <= self.bt_temp < 31:
                print("The tank pressure is in range")
                self.bt_status = "BT_PSI_READY"
        except Exception as e:
            print(e)

    def psi_choice(self):
        """
        Method that allows a user to choose between manual and automatic operation of pressure controls. Allows PSI between 1 and 30.

        :return:  Sets the brite tank pressure to values between 1 and 30 PSI
        """
        selection = False
        while not selection:
            choice = input("Would you like to Manually or Automatically Adjust PSI? Enter (M/A) or (N) to exit: ")
            if choice in ['m', 'M', 'manual', 'Manual', 'MANUAL', 'manually', 'Manually', 'MANUALLY']:
                selection = True
                psi_ready = False
                while not psi_ready:
                    print("You have selected Manual PSI operation.")
                    new_psi = float(input(
                        "When the brite tank has reached your desired pressure, enter its value (PSI): "))
                    if 1 <= new_psi < 31:
                        psi_ready = True
                        self.update_bt_psi(new_psi)
                    else:
                        print("")
                        print("Please adjust the pressure between 1 and 30 PSI.")
                self.print_carb_status()
            elif choice in ['a', 'A', 'auto', 'Auto', 'AUTO', 'automatically', 'Automatically', 'AUTOMATICALLY']:
                selection = True
                psi_ready = False
                while not psi_ready:
                    print("You have selected Automatic PSI operation.")
                    target_psi = float(input("Enter the target pressure (PSI): "))
                    if 1 <= target_psi < 31:
                        psi_ready = True
                        self.auto_psi(target_psi) # contains the simulated delay value for pressure adjustments for pressure values
                    else:
                        print("")
                        print("Please enter a pressure between 1 and 30 PSI.")
            elif choice in ['N','n','no','No','NO']:
                selection = True

    def auto_psi(self, target_psi):
        """
        Method that simulates automatic PSI adjustment through a delay.

        :param target_psi: the target brite tank pressure in PSI
        :return: Sets the pressure in the brite tank to the specified PSI
        """
        while self.bt_psi != target_psi:
            time.sleep(sim_sleep_mod)
            if self.bt_psi < target_psi and abs(self.bt_psi - target_psi) >= 1:
                self.bt_psi += 1
            elif self.bt_psi > target_psi and abs(self.bt_psi -target_psi) >= 1:
                self.bt_psi -= 1
            elif abs(self.bt_psi - target_psi) < 1 or self.bt_psi == target_psi:
                self.bt_psi = target_psi
            else:
                print("Error")
            self.print_carb_status()
        return self.bt_psi

    def auto_carb(self, target_carb):
        """
        Method that simulates the automatic adjustment of PIS to a targeted carbonation level in CO2 vols
        :param target_carb: the target bright beer CO2 volume
        :return: Sets the pressure in the brite tank to adjust to a specified CO2 volume
        """
        carbonation_ready = False
        while not carbonation_ready and 2 <= self.bt_psi < 31:
            time.sleep(sim_sleep_mod)
            if self.get_carbonation() < target_carb:
                self.bt_psi += 1
                if self.get_carbonation() > target_carb:
                    carbonation_ready = True
            elif self.get_carbonation() > target_carb:
                self.bt_psi -= 1
            elif self.get_carbonation() == target_carb:
                carbonation_ready = True
            else:
                print("Error")
            self.print_carb_status()

    def start_brite_tank(self, batch_id):
        """
        Main Brite Tank Method for reaching the correct carbonation level through simulation

        :return: Sets the temperature and pressure to correct values in order to reach a targeted carbonation volume
        """
        try:
            # Print Initial Status Message
            self.print_carb_status()
            print("Welcome to the Kegging Process")

            # Run initial temperature control and log
            self.bt_temp_control()
            bt_temp_log = "Brite Tank Temperature in Range"
            self.bt_log(batch_id,"Kegging",bt_temp_log)

            #Run initial pressure control and log
            self.bt_psi_control()
            bt_psi_log = "Brite Tank Pressure in Range"
            self.bt_log(batch_id,"Kegging",bt_psi_log)

            # Currently Manual input for target carbonation, can substitute from recipe pull from ServicenNow
            recipe_carb = float(input("Please enter the target carbonation volume: "))

            # Simulated Automatic pressure adjustment to hit targeted PSI, aims to overshoot rather than undershoot because opening valves loses pressure
            self.auto_carb(recipe_carb)
            bt_carb_log = "Carbonation Ready at " + str(self.get_carbonation()) + " volumes"
            self.bt_log(batch_id, "Kegging", bt_carb_log)

            # Send Ready for QA Test Messaage
            print("The Batch is ready for Quality Assurance Taste Tests")
            bt_carb_end_log = "Ready for QA Test"
            self.bt_status = "QA_READY"
            self.bt_log(batch_id, "Kegging", bt_carb_end_log)

        except Exception as e:  # error handling
            print(e)

    def bt_log(self, batch_id, bb_stage, log_message):
        """
        Logging Method for the Brite Tank Class.

        :param batch_id: The batch ID of the current batch
        :param bb_stage: The current Brewing Stage
        :param log_message: The main log message
        :return: Sends a log to ServiceNow with timestamp appended to the beginning of the log message

        """
        currentTimeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        status_log = "{\"batch_id\":\"" + str(batch_id) + "\", \"brew_batch_stage\":\"" + str(bb_stage) + "\", \"log\":\"" + currentTimeStamp + " " + str(log_message) + "\"}"
        #ServiceNowLog.ServiceNowLog.create_new_log(self, status_log)
        bt_loglist.append(status_log)

    def get_bt_loglist(self):
        """
        Method that returns a list of the brite tank log
        :return: returns the brite tank log as a list
        """
        return bt_loglist

