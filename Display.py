import Bank
class Display:
    def __init__(self, bank):
        self.bank = bank
    def start(self):
        # inital display setup
    def showMessage(self,msg):
        # display message
    def showInput(self,code):
        # display string representing user input for product code
    def refresh(self):
        # update display of inserted money state using "bank" attribute