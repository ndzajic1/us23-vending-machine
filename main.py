from Bank import Bank
from Display import Display
from Keypad import Keypad
import machine
from machine import Pin, Timer

import time

# initial money in the machine
INIT_BALANCE10kf = 0
INIT_BALANCE2KM = 0

bank = Bank(INIT_BALANCE10kf, INIT_BALANCE2KM)
display = Display(bank)
keypad = Keypad(display)

# Pin numbers for sensors detecting inserted coins
PIN_10kf = 9 
PIN_2KM = 10

detector10kf = Pin(PIN_10kf, Pin.IN)
detector2KM = Pin(PIN_2KM, Pin.IN)

# for storing last detection to detect future changes of sensors state
lastDetection10kf = int(0)
lastDetection2KM = int(0)

# detecting sensor state changes, storing the value of inserted coins
def moneyDetector(p):
    global lastDetection10kf, lastDetection2KM
    if detector10kf.value() != lastDetection10kf:
        bank.addToBank(0.10)
        display.refresh()
        lastDetection10kf = detector10kf.value()
        time.sleep(2)
    elif detector2KM.value() != lastDetection2KM:
        bank.addToBank(2.00)
        display.refresh()
        lastDetection2KM = detector2KM.value()   
        time.sleep(2)
   
watchForCoins = Timer( callback = moneyDetector,
                       mode = Timer.PERIODIC,
                       period = 1
                     )


# Pin numbers for solenoids and estimated times for 1 and 0
SOL10kf_PIN = 4
SOL2KM_PIN = 5
WAIT_SOL10kf_ON = 0.15
WAIT_SOL10kf_OFF = 1
WAIT_SOL2KM_ON = 0.17
WAIT_SOL2KM_OFF = 1

returner10kf = Pin(SOL10kf_PIN, Pin.OUT)
returner2KM = Pin(SOL2KM_PIN, Pin.OUT)

# returning money handler, controlling solenoids here
def moneyReturner(coins10kf, coins2KM):
  # global bank
    for _ in range(coins10kf):
        returner10kf.on()
        time.sleep(WAIT_SOL10kf_ON)
        returner10kf.off()
        time.sleep(WAIT_SOL10kf_OFF)
    for _ in range(coins2KM):
        returner2KM.on()
        time.sleep(WAIT_SOL2KM_ON)
        returner2KM.off()
        time.sleep(WAIT_SOL2KM_OFF)
    lastDetected10kf = 3
    lastDetected2KM = 3
    #returnedMoney = 0.1 * coins10 + 0.5 * coins50
    #bank.returnMoney(returnedMoney)

# product codes with their prices, stored in dictionary where key = code, value = price"
products = {
            "A01": 1.80,
            "A02": 2.00,
            "A03": 2.10,
            "-"  : 0
            }

# Pin numbers for leds signalising product purchase
LED_PROD1 = 14
LED_PROD2 = 13
LED_PROD3 = 12

# objects for controlling leds, stored in dictionary where key = code, value = pin
leds = {
        "A01": Pin(LED_PROD1, Pin.OUT),
        "A02": Pin(LED_PROD2, Pin.OUT),
        "A03": Pin(LED_PROD3, Pin.OUT),
        "A__": Pin(13, Pin.OUT)
        }

# time for led to be on
LED_WAIT_TIME = 5
def signalisePurchase(product): 
    leds[product].on()
    time.sleep(LED_WAIT_TIME)
    leds[product].off()
    

while True:
    print("thr")
    display.refresh()
    code = keypad.input()
    while not code in products:
        display.showMessage("Netacan kod")
        #code = "-"
        time.sleep(3)
        display.showMessage("Odaberite artikl:")
        code = keypad.input()
    if products[code] > bank.sessionMoney():
        display.showMessage("Nedovoljno novca.")
        code = "-"
        time.sleep(3)
        display.showMessage("Odaberite artikl:")
    #inputMoney = bank.sessionMoney()
    print("code:" + code + ", money = " + str(bank.sessionMoney()) + ",prod:"+str(products[code]))
    coins2Return = bank.calculateChange(products[code]) # tuple
    print("(" + str(coins2Return[0]) + "," + str(coins2Return[1]))
    
    signalisePurchase(code)
        #time.sleep(2)
    moneyReturner(coins2Return[0], coins2Return[1])
    time.sleep(2)
    bank.sessionStart()
    display.refresh()
    time.sleep(4)
    #if inputMoney == (coins2Return[0] * 0.10 + coins2Return[1] * 2.00):
    #    continue
    #bank.sessionStart()
    



