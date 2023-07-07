from Bank import Bank
from Display import Display
from Keypad import Keypad
import machine
from machine import Pin, Timer

import time

# initial balance of coins in the machine
INIT_BALANCE10kf = 0
INIT_BALANCE2KM = 0

# helper objects
bank = Bank(INIT_BALANCE10kf, INIT_BALANCE2KM)
display = Display(bank)
keypad = Keypad(display)

# pin numbers for microswitches detecting inserted coins
PIN_10kf = 9 
PIN_2KM = 10

# declaring pins
detector10kf = Pin(PIN_10kf, Pin.IN)
detector2KM = Pin(PIN_2KM, Pin.IN)

# for storing last detection to detect future changes of microswitches' states
lastDetection10kf = int(0)
lastDetection2KM = int(0)

# detecting microswitches' states changes, adding money to bank, and updating display
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

# previous function to be called on timer, simulating interrupt   
watchForCoins = Timer( callback = moneyDetector,
                       mode = Timer.PERIODIC,
                       period = 1
                     )


# pin numbers for solenoids and estimated on and off times 
SOL10kf_PIN = 4
SOL2KM_PIN = 5

WAIT_SOL10kf_ON = 0.15
WAIT_SOL10kf_OFF = 1
WAIT_SOL2KM_ON = 0.17
WAIT_SOL2KM_OFF = 1

# pin objects for solenoids
returner10kf = Pin(SOL10kf_PIN, Pin.OUT)
returner2KM = Pin(SOL2KM_PIN, Pin.OUT)

# returning money handler, controlling solenoids here
def moneyReturner(coins10kf, coins2KM):
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

# product codes with their prices, stored in dictionary where key = code, value = price"
products = {
            "A01": 1.80,
            "A02": 2.00,
            "A03": 2.10,
            "-"  : 0
            }

# pin numbers for leds signalising product purchase
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

# purchase signalisation by turning led on and off
def signalisePurchase(product): 
    leds[product].on()
    time.sleep(LED_WAIT_TIME)
    leds[product].off()
    
# main event loop
while True:
    # set display
    display.refresh()

    # wait for customer input
    code = keypad.input()

    # restart when code invalid
    while not code in products:
        display.showMessage("Netacan kod")
        time.sleep(3)
        display.showMessage("Odaberite artikl:")
        code = keypad.input()

    # not enough money inserted
    if products[code] > bank.sessionMoney():
        display.showMessage("Nedovoljno novca.")
        code = "-"
        time.sleep(3)
        display.showMessage("Odaberite artikl:")

    # purchase successful, return coins and signalise it by corresponding led
    coins2Return = bank.calculateChange(products[code]) # tuple
    signalisePurchase(code)
    moneyReturner(coins2Return[0], coins2Return[1])
    time.sleep(2)

    # session is over, restart and refresh display
    bank.sessionStart()
    display.refresh()
    time.sleep(4)
    



