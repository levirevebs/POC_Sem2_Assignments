class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2



tri1 = RightTriangle(3, 4)
print("The area of tri1 is", tri1.area())
tri2 = RightTriangle(6, 8)
print("The area of tri2 is", tri2.area())


    
