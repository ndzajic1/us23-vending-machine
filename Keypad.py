import Display
class Keypad:
    def __init__(self, display):
        self.display = display
        self.input = "___"
        
    def input(self):
        # handle user input here, communication with display via display attribute