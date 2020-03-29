#!/usr/bin/python
import sys
import Adafruit_DHT
import re
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

sensor = 11
pin = 4

# button for sanitization
s_button_pin = 26 # UP key
# button for temperature
t_button_pin = 13 # DOWN key

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)

# function for display msg in led matrix
def display_msg_in_led_matrix(msg,color):
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=1, block_orientation=90, rotate=0)
    show_message(device, msg, fill=color, font=proportional(CP437_FONT), scroll_delay=0.1)

# function for display msg in LCD
def display_msg_in_lcd(msg):
    # Turn backlight on
    lcd.set_backlight(0)
    lcd.clear()
    lcd.message(msg)
    for i in range(lcd_columns-len(msg)):
        time.sleep(0.5)
        lcd.move_right()
    for i in range(lcd_columns-len(msg)):
        time.sleep(0.5)
        lcd.move_left()

# Pin setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(s_button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(t_button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    print("\n      Press up button when sanitization is done.")
    GPIO.wait_for_edge(s_button_pin,GPIO.FALLING)
    message = '  Sanitization \n   Completed'
    print("\t\t" + message.replace(" \n ",""))
    display_msg_in_lcd(message)
    try:
        print("\n      press down button to measure temperature.")
        GPIO.wait_for_edge(t_button_pin,GPIO.FALLING)
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        temperature = 9.0/5.0 * temperature + 32
        print('\t\t   Temp={0:0.1f}* F'.format(temperature))
        while( temperature > 70 or temperature < 60):
            display_msg_in_led_matrix(msg = str(temperature),color="red")
            display_msg_in_lcd(str(temperature))
	    print("\t Temperature of yeast is out of range \n")
            print("      press down button to measure temperature.")
            GPIO.wait_for_edge(t_button_pin,GPIO.FALLING)
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
            temperature = 9.0/5.0 * temperature + 32
            print('\t\t   Temp={0:0.1f}* F'.format(temperature))
       	    display_msg_in_led_matrix(msg = str(temperature),color="green")
        display_msg_in_lcd(str(temperature))
        print("\t   temperature is in range.\n")
    except:
        GPIO.cleanup()
except:
    GPIO.cleanup()
GPIO.cleanup()
 
