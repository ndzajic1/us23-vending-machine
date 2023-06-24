class Bank:
    def __init__(self, initialBalance):
        self.balance = initialBalance
        self.session = 0
    def sessionStart(self):
        self.session = 0
    def addToBank(self,money):
        self.balance += money
        self.session += money
    def returnMoney(self,change):
        self.balance -= change
    def getCurrentBalance(self):
        return self.balance
    def getCurrentSession(self):
        return self.session