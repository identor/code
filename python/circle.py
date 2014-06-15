import math

class Circle:
    def __init__(self, radius=1):
        # a private field
        self.__radius = radius

    def perimeter(self):
        return 2 * self.__radius * math.pi

    def area(self):
        return self.__radius**2 * math.pi

    def set_radius(self, radius):
        self.__radius = radius

def main():
    radius = eval(input("Enter the radius of a circle: "))
    circle = Circle(radius)
    print("The area of the circle is", circle.area())

main()
input("Press Enter to continue...")
