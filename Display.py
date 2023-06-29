from Bank import Bank
from ili934xnew import ILI9341, color565
from machine import Pin, SPI, ADC
from micropython import const
import os
import glcdfont
import tt14
import tt24
import tt32
import time

class Display:
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
    
    def __init__(self, bank):
        self.bank = bank
        spi = SPI(   0,
                     baudrate=62500000,
                     miso=Pin(TFT_MISO_PIN),
                     mosi=Pin(TFT_MOSI_PIN),
                     sck=Pin(TFT_CLK_PIN)
                  )
        self.display = ILI9341(  spi,
                                 cs=Pin(TFT_CS_PIN),
                                 dc=Pin(TFT_DC_PIN),
                                 rst=Pin(TFT_RST_PIN),
                                 w=SCR_WIDTH,
                                 h=SCR_HEIGHT,
                                 r=SCR_ROT
                               )

        self.display.set_font(tt32)
        self.display.rotation=3
        self.display.init()
        
        self.message = "Ubacite kovanicu:"
        self.code = "_ _ _"
        
        
    def refresh(self):
        # inital display setup
        self.display.erase()
        self.display.set_pos(50,50)
        self.display.print(self.message)
        self.display.set_pos(50,100)
        formattedNumber = "{:.2f}".format(self.bank.sessionMoney())
        self.display.print("Kredit: " + str(formattedNumber) + " KM")    
        self.display.set_pos(100,150)
        self.display.print(self.code)
                      
    def showMessage(self,msg):
        self.message = msg
        self.refresh()
        
    def showInput(self,code):
        self.code = code[0] + " " + code[1] + " " + code[2]
        self.refresh()

