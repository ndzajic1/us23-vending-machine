class Bank:
    def __init__(self, initialBalance10kf, initialBalance2KM):
        self.balance10kf = initialBalance10kf
        self.balance2KM = initialBalance2KM
        self.session = 0
        
    def sessionStart(self):
        self.session = 0
        
    def addToBank(self, money):
        if money == 0.10:
            self.balance10kf += 1
        else:
            self.balance2KM += 1
        self.session += money
        
    def calculateChange(self, productPrice):
        
        change = int((self.session - productPrice) * 100 + 0.5)

        if change < 0:
            return calculateChange(0)

        coins2KM = int(change // 200)
        change -= coins2KM * 200
        coins10kf = int(change // 10)
        print(coins10kf)
        if self.balance10kf < coins10kf:
            return self.calculateChange(0)
        
        elif self.balance2KM < coins2KM:
            coins10 += (coins2KM - self.balance2KM) * 20
            coins2KM = self.balance2KM
            if self.balance10kf < coins10kf:
                return self.calculateChange(0)
            
        self.balance2KM -= coins2KM
        self.balance10kf -= coins10kf
        self.session -= productPrice

        return (coins10kf, coins2KM)
    
    def sessionMoney(self):
        return self.session

