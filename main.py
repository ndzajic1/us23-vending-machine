import Keypad
import Display
import machine
from machine import Pin
import time

# initial money in the machine
# INIT_BALANCE10 =
# INIT_BALANCE50 =
bank = Bank(INIT_BALANCE10, INIT_BALANCE50)
display = Display(bank)
keypad = Keypad(display)

# Pin numbers for sensors detecting inserted coins
# KF10_PIN = 
# KF50_PIN =

detector10 = Pin(KF10_PIN, Pin.IN)
detector50 = Pin(KF50_PIN, Pin.IN)

detector10.irq(
               handler = lambda p: (
                            bank.addToBank(10),
                            display.refresh()
                                    ),
               trigger = Pin.IRQ_FALLING | Pin.IRQ_RISING
               )
detector50.irq(
               handler = lambda p: (
                            bank.addToBank(50),
                            display.refresh()
                                    ),
               trigger = Pin.IRQ_FALLING | Pin.IRQ_RISING
               )

# Pin numbers for solenoids and estimated times for 1 and 0
# SOL10_PIN = 
# SOL50_PIN =
# WAIT_SOL_ON =
# WAIT_SOL_OFF =

returner10 = Pin(SOL10_PIN, Pin.OUT)
returner50 = Pin(SOL50_PIN, Pin.OUT)

# returning money handler, controlling solenoids here
def moneyReturner(coins10, coins50):
  # global bank
    for _ in range(coins10):
        returner10.on()
        time.sleep(WAIT_SOL_ON)
        returner10.off()
        time.sleep(WAIT_SOL_OFF)
    for _ in range(coins50):
        returner50.on()
        time.sleep(WAIT_SOL_ON)
        returner50.off()
        time.sleep(WAIT_SOL_OFF)
    #returnedMoney = 0.1 * coins10 + 0.5 * coins50
    #bank.returnMoney(returnedMoney)

# product codes with their prices, stored in dictionary where key = code, value = price"
products = {
            "A01": 80,
            "A02": 120,
            "A03": 150,
            "-"  : 0;
            }

# Pin numbers for leds signalising product purchase
# PROD1_LED =
# PROD2_LED =
# PROD3_LED =
# objects for controlling leds, stored in dictionary where key = code, value = pin
leds = {
        "A01": Pin(PROD1_LED, Pin.OUT),
        "A02": Pin(PROD2_LED, Pin.OUT),
        "A03": Pin(PROD3_LED, Pin.OUT)
        }

# time for led to be on
# LED_WAIT_TIME =
def signalisePurchase(product): 
    leds[product].on()
    time.sleep(LED_WAIT_TIME)
    leds[product].off()
    
#    
while True:
    bank.sessionStart()
    display.start()
    code = keypad.input()
    if not code in products:
        display.showMessage("Ne postoji artikl s tim kodom.")
        code = "-"
    elif products[code] > bank.sessionMoney():
        display.showMessage("Niste ubacili dovoljno love.")
        code = "-"
    inputMoney = bank.sessionMoney()
    coins2Return = bank.calculateChange(products[code]) # tuple
    moneyReturner(coins2Return[0], coins2Return[1])
    if (inputMoney == coins2Return[0]*10 + coins2Return[1]*50) : continue
    signalisePurchase(code)
