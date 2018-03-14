#!/usr/bin/python
#show IP address on the LCD Plate at startup
##Mbeckma7

import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

displayText = "Godd Afternoon"

lcd.clear()
lcd.message(displayText)

