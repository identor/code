from rational import Rational

def main():
    print("Input a rational number. Eg: for 1/6 enter 1, 6.")
    n1, d1 = eval(input("fraction one: "))
    n2, d2 = eval(input("fraction two: "))
    r1 = Rational(n1, d1)
    r2 = Rational(n2, d2)
    print()
    print("Operations for", r1, "and", r2, ":")
    print(r1, "+", r2, "=", r1 + r2)
    print(r1, "-", r2, "=", r1 - r2)
    print(r1, "*", r2, "=", r1 * r2)
    print(r1, "/", r2, "=", r1 / r2)
    print("Is", r1, "less than", r2, ":", r1 < r2)
    print("Is", r1, "less than or equal", r2, ":", r1 <= r2)
    print("Is", r1, "equal", r2, ":", r1 == r2)
    print("Is", r1, "not equal to", r2, ":", r1 != r2)
    print("Is", r1, "greater than", r2, ":", r1 > r2)
    print("Is", r1, "greater than or equal", r2, ":", r1 >= r2)

main()
input("Press Enter to Continue...")
