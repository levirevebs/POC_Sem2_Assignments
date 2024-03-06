class Rectangle:
    def __init__(self, base: float, height: float) -> None:
        self.__base = base
        self.__height = height
        
    def get_height(self) -> float:
        return self.__height

    def get_base(self) -> float:
        return self.__base
  
    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height

    def get_area(self) -> float:
        return self.__base * self.__height

good_rectangle = Rectangle(5, 3)
print("base is:",good_rectangle.base)
print("height is:",good_rectangle.height)
print("base is:",good_rectangle.base)
print("base is:",good_rectangle.base)

# did not finish in class time!!!???!!!