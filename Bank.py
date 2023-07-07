# class for business logic of payments and returning change
class Bank:
    
    # constructing Bank object with initial balance of each coin
    def __init__(self, initialBalance10kf, initialBalance2KM):
        self.balance10kf = initialBalance10kf
        self.balance2KM = initialBalance2KM
        self.session = 0.00

    # new customer's session starts   
    def sessionStart(self):
        self.session = 0

    # updating balance when coin is inserted    
    def addToBank(self, money):
        if money == 0.10:
            self.balance10kf += 1
        else:
            self.balance2KM += 1
        self.session += money

    # simple algorithm to calculate how many 10kf and 2KM coins to return as change 
    def calculateChange(self, productPrice):
        
        change = int((self.session - productPrice) * 100 + 0.5)
        if change == 0:
            return (0,0)
        elif change < 0:
            return self.calculateChange(0.00)
        
        coins2KM = int(change // 200)
        change -= coins2KM * 200

        coins10kf = int(change // 10)

        self.balance2KM -= coins2KM
        self.balance10kf -= coins10kf
        self.session -= productPrice

        return (coins10kf, coins2KM)

    # session money getter
    def sessionMoney(self):
        return self.session

