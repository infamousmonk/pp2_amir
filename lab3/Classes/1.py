class getString:
    def __init__(self, s):
        self.s=s
    def printString(self):
        print("Uppercase: " + self.s.upper())

s=input("Type something: ")
answer = getString(s)
answer.printString()