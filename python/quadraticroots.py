import math

a, b, c = eval(input("Coefficients of Quadratic Equation (a, b, c): "))

discriminant = math.sqrt((b ** 2) - (4 * a * c))

if discriminant > 0:
    rootOne = (-b + discriminant) / (2 * a)
    rootTwo = (-b - discriminant) / (2 * a)
    print("The roots of the equation are", rootOne, rootTwo)

elif discriminant == 0:
    root = -b / 2 * a
    print("The root of the equation is: ", root)

else:
    print("The root of the equation is Imaginary")


input("Press Enter to continue...")
