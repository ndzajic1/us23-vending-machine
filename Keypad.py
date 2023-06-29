from machine import Pin
import time
from Display import Display

row = [Pin(21,Pin.OUT),Pin(22,Pin.OUT),Pin(26,Pin.OUT),Pin(27,Pin.OUT)]
col = [Pin(0, Pin.IN),Pin(1, Pin.IN),Pin(2, Pin.IN),Pin(3, Pin.IN)]
symbol = [['1','2','3','A'],['4','5','6','B'],
    ['7','8','9','C'],['*','0','#','D']]

class Keypad:
    def __init__(self, display):
        self.display = display
        
    def input(self):
        # handle user input here, communication with display via display attribute
        code = ['_', '_', '_']  # Use a list to store the input code
        numOfSymbols = 0  # counts number of inputed symbols

        self.display.showInput(code)
        while True:
            # Use < instead of != for the symbol count
            for i in range(4):
                row[i].value(1)
                for j in range(4):
                    if col[j].value() == 1:
                        while col[j].value() == 1:
                            pass
                        if symbol[i][j] == '#':
                            return "".join(code)
                        if numOfSymbols == 0:
                            code = ['_', '_', '_'] 
                        code[numOfSymbols] = symbol[i][j]
                        numOfSymbols += 1
                        if numOfSymbols == 3:
                            numOfSymbols = 0
                        self.display.showInput(code)
                row[i].value(0)
 

