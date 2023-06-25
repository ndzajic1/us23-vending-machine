class Bank:
    def __init__(self, self.balance10, self.balance50):
        self.balance50 = initialBalance50
        self.balance10 = initialBalance10
        self.session = 0
        
    def sessionStart(self):
        self.session = 0
        
    def addToBank(self, money):
        if (money // 50) > 0
            self.balance50 += money//50
        else
            self.balance10 += money//10
        self.session += money
        
    def calculateChange(self, productPrice):
        self.session -= productPrice
        #self.balance -= self.session
        coins50 = int(self.session//50)
        coins10 = int((self.session % 50) / 10)
        
        if self.balance10 < coins10:
            self.session += productPrice
            return self.calculateChange(0)
        
        elif self.balance50 < coins50:
            coins10 += (coins50 - self.balance50) * 5
            coins50 = self.balance50
            if self.balance10 < coins10:
                self.session += productPrice
                return self.calculateChange(0)
            
        self.balance50 -= coins50
        self.balance10 -= coins10
        return (coins10, coins50)
    
    def getCurrentSession(self):
        return self.session
