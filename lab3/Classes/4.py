import math
class Point:
    def __init__(self, x, y, dx, dy):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
    def show(self):
        print("(" + str(self.x) + "," + str(self.y) + ")")
    def move(self):
        print("(" + str(self.x+self.dx) + "," + str(self.y+self.dy) + ")")
    def dist(self):
        print(math.sqrt((self.dx)**2+(self.dy)**2))
x=int(input("Type x: "))
y=int(input("Type y: "))
dx=int(input("The steps you want x to move: "))
dy=int(input("The steps you want y to move: "))
answer = Point(x, y, dx, dy)
answer.show()
answer.move()
answer.dist()