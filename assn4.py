class Rectangle():
    __counter = 0

    def __init__(self, base, height):
        self.__base = base
        self.height = height
        Rectangle.__counter += 1

    def get_count(Rectangle):
        return Rectangle.__counter

goodie = Rectangle(65, 4)
goodie2 = Rectangle(5, 2)
Rectangle.get_count()

print(goodie)
print(goodie2)