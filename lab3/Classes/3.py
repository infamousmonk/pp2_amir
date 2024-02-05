class Shape:
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        print("The area is: " + str(self.length * self.width))
        
class Rectangle(Shape):
    def __init__ (self, length, width):
        Shape.__init__(self, length, width)
length = int(input("Type length: "))
width = int(input("Type width: "))
answer = Rectangle(length, width)
answer.area()