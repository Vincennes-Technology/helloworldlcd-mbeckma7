#!/usr/bin/python
#show IP address on the LCD Plate at startup
##Mbeckma7

import Adafruit_CharLCD as LCD
import time
import subprocess

lcd = LCD.Adafruit_CharLCDPlate()
Name = subprocess.check_output(['hostname']).strip()
IPaddr = subprocess.check_output(['hostname', '-I'])

DisplayText = 'hello world'
DisplayText1 = Name + '\n' + IPaddr
Refresh = True


while (True):
    if lcd.is_pressed(LCD.SELECT):
        lcd.clear()
        lcd.message('hello world\n')
        Refresh = True
        time.sleep(0.5)
    else:
        if Refresh:
            lcd.clear()
            lcd.message(DisplayText1 + '\n')
            time.sleep(0.5)
            Refresh = False

