import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def discriminant(self):
        return self.__b**2 - 4*self.__a*self.__c
    
    def root_count(self):
        d = self.discriminant()
        return 2 if d > 0 else 1 if d == 0 else 0

    def root_one(self):
        return (-self.__b + math.sqrt(self.discriminant())) / 2*self.__a
    
    def root_two(self):
        return (-self.__b - math.sqrt(self.discriminant())) / 2*self.__a

# test
def main():
    a, b, c = eval(input("Coefficients of Quadratic Equation (a, b, c): "))
    eq = QuadraticEquation(a, b, c)
    if eq.root_count() == 2:
        print("roots:", eq.root_one(), ",", eq.root_two())
    elif eq.root_count() == 1:
        print("root:", eq.root_one())
    else:
        print("The root is imaginary")

main()
input("Press Enter to continue...")
