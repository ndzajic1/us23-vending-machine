import Bank
from ili934xnew import ILI9341, color565
from machine import Pin, SPI, ADC
from micropython import const
import os
import glcdfont
import tt14
import tt24
import tt32
import time

# Dimenzije displeja
SCR_WIDTH = const(320)
SCR_HEIGHT = const(240)
SCR_ROT = const(2)
CENTER_X = int(SCR_WIDTH/2)
CENTER_Y = int(SCR_HEIGHT/2)

# Podešenja SPI komunikacije sa displejem
TFT_CLK_PIN = const(18)
TFT_MOSI_PIN = const(19)
TFT_MISO_PIN = const(16)
TFT_CS_PIN = const(17)
TFT_RST_PIN = const(20)
TFT_DC_PIN = const(15)

spi = SPI(
 0,
 baudrate=62500000,
 miso=Pin(TFT_MISO_PIN),
 mosi=Pin(TFT_MOSI_PIN),
 sck=Pin(TFT_CLK_PIN))
display = ILI9341(
 spi,
 cs=Pin(TFT_CS_PIN),
 dc=Pin(TFT_DC_PIN),
 rst=Pin(TFT_RST_PIN),
 w=SCR_WIDTH,
 h=SCR_HEIGHT,
 r=SCR_ROT)

display.set_font(tt24)
display.rotation=3
display.init()

class Display:
    def __init__(self, bank):
        self.bank = bank
    def start(self):
        # inital display setup
        display.set_pos(100,100)
        display.print("Balance: " + str(bank.sessionMoney())
    
        display.set_pos(100,140)
        display.print("Code: ___")
                      
    def showMessage(self,msg):
        # display message
    def showInput(self,code):
        # display string representing user input for product code
    def refresh(self):
        # update display of inserted money state using "bank" attribute
