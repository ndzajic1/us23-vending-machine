import machine
from machine import Pin
import time
cifre = [Pin(4,Pin.OUT), Pin(5,Pin.OUT), Pin(6,Pin.OUT), Pin(7,Pin.OUT)]
# dp,g,f,e,d,c,b,a
segm = [Pin(15,Pin.OUT), Pin(14,Pin.OUT), Pin(13,Pin.OUT), Pin(12,Pin.OUT),
    Pin(11,Pin.OUT), Pin(10,Pin.OUT), Pin(9,Pin.OUT), Pin(8,Pin.OUT)]
#brojevi 0-9 na displayu
display0 = [[1,1,0,0,0,0,0,0], [1,1,1,1,1,0,0,1], [1,0,1,0,0,1,0,0],
    [1,0,1,1,0,0,0,0], [1,0,0,1,1,0,0,1], [1,0,0,1,0,0,1,0],
    [1,0,0,0,0,0,1,0], [1,1,1,1,1,0,0,0], [1,0,0,0,0,0,0,0],
    [1,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]]
def postaviCifru(k):
    for i in range(8):
        segm[i].value(display0[k][i])
red = [Pin(21,Pin.OUT),Pin(22,Pin.OUT),Pin(26,Pin.OUT),Pin(27,Pin.OUT)]
kol = [Pin(0, Pin.IN),Pin(1, Pin.IN),Pin(2, Pin.IN),Pin(3, Pin.IN)]
simbol = [['1','2','3','A'],['4','5','6','B'],
    ['7','8','9','C'],['*','0','#','D']]
def ocitaj():
    for i in range(4):
        red[i].value(1);
        for j in range(4):
            if kol[j].value() == 1:
                while kol[j].value() == 1:
                    pass
                red[i].value(0)
                return simbol[i][j]
        red[i].value(0)
    return chr(0)
pin = "0000"
pinCheck = [pin[0],pin[1],pin[2],pin[3]]
pogresnihUnosa = 0
unos = [chr(58), chr(58), chr(58), chr(58)]
#tacke
tacke0 = [0,1,1,1,1,1,1,1]
tacke1 = [1,0,0,0,0,0,0,0]
def ispravanUnos():
    global pogresnihUnosa
    for i in range(25):
        for i in range(4):
            cifre[i].value(0)
            for k in range(8):
                segm[k].value(tacke0[k])
            time.sleep(.025)
            postaviCifru(10)
            time.sleep(.025)
            cifre[i].value(1)
    pogresnihUnosa = 0
#minusi
minus0 = [1,0,1,1,1,1,1,1]
minus1 = [0,1,0,0,0,0,0,0]
def neispravanUnos():
    for i in range(25):
        for i in range(4):
            cifre[i].value(0)
            for k in range(8):
                segm[k].value(minus0[k])
            time.sleep(.025)
            postaviCifru(10)
            time.sleep(.025)
            cifre[i].value(1)
def neispravanUnos3x():
    for brojac in range(10):
        for i in range(50):
            b = int(brojac)
            for i in range(4):
                cifre[3 - i].value(0)
                postaviCifru(int (b % 10))
                time.sleep(.005)
                b = int(b / 10)
                postaviCifru(10)
                cifre[3 - i].value(1)
def prikaziUnos():
    for i in range(4):
        cifre[i].value(0)
        postaviCifru(ord(unos[i])-ord('0'))
        time.sleep(.005)
        postaviCifru(10)
        cifre[i].value(1)
def provjeriPin():
    global unos, pogresnihUnosa
    if pinCheck != unos:
        pogresnihUnosa += 1
        if pogresnihUnosa == 3:
            neispravanUnos3x()
            pogresnihUnosa = 0
        else:
            neispravanUnos()
    else:
        ispravanUnos()
        pogresnihUnosa = 0
        
unos = [chr(58), chr(58), chr(58), chr(58)]

for i in range(4):
    cifre[i].value(1)
    
while True:
    ref = 0
    for i in range(4):
        while True:
            prikaziUnos()
            c = ocitaj()
            if ord(c) - ord('0') >= 0 and ord(c) - ord('0') <= 9:
                unos[i] = c
                break
            elif c == '#':
                provjeriPin()
                ref = -1
                break
        if ref == -1:
            break




