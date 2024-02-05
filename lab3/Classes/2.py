class Shape:
    def __init__ (b, shape):
        b.shape=shape
        
    def area1(b):
        S1 = b.shape * b.shape
        print("Area is: " + str(S1))
        
class Square(Shape):
    def __init__(b, shape):
        Shape.__init__(b, shape)

length=int(input("Type the length: "))
answer=Square(length)
answer.area1()