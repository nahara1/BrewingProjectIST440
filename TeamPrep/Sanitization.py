import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDBackpack(address=0x21)

button_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
        time.sleep(0.3)

        # Turn backlight on
        lcd.set_backlight(0)
        if(GPIO.input(button_pin) == 0):
            lcd.clear()
            message = '  Sanitization \n   Completed'
            lcd.message(message)
            for i in range(lcd_columns-len(message)):
                time.sleep(0.5)
                lcd.move_right()
            for i in range(lcd_columns-len(message)):
                time.sleep(0.5)
                lcd.move_left()
            #print("sanitization complete")
        break