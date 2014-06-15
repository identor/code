NUM = 0
DEN = 1

def gcd(num1, num2):
    high = max(num1, num2)
    low = min(num1, num2)

    divisor = high
    for i in range(high, 0, -1):
        if low % divisor == 0 == high % divisor : return divisor
        divisor -= 1
        
    return None
        
    

class Rational:
    def __init__(self, numerator=0, denominator=1):
        self.__num = numerator
        self.__den = denominator
        self.simplify()

    def __add__(self, other):
        num = self[NUM]*other[DEN] + other[NUM]*self[DEN]
        den = self[DEN] * other[DEN]
        return Rational(num, den)

    def __sub__(self, other):
        num = self[NUM]*other[DEN] - other[NUM]*self[DEN]
        den = self[DEN] * other[DEN]
        return Rational(num, den)

    def __mul__(self, other):
        num = self[NUM] * other[NUM]
        den = self[DEN] * other[DEN]
        return Rational(num, den)
    
    def __truediv__(self, other):
        num = self[NUM] * other[DEN]
        den = self[DEN] * other[NUM]
        return Rational(num, den)

    def __cmp__(self, other):
        self_val = self.__num / self.__den
        other_val = other[NUM] / other[DEN]
        result = 0

        if self_val > other_val:
            result = 1
        elif self_val < other_val:
            result = -1
        else:
            result = 0
        
        return result

    def __lt__(self, other):
        return self.__cmp__(other) == -1

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __ne__(self, other):
        return self.__cmp__(other) != 0

    def __gt__(self, other):
        return self.__cmp__(other) == 1

    def __ge__(self, other):
        return self.__cmp__(other) >= 0

    def __int__(self, other):
        return int(self.__num / self.__den)

    def __float__(self, other):
        return self.__num / self.__den

    def __str__(self):
        return str(self.__num) + "/" + str(self.__den)    

    def __getitem__(self, item):
        return self.__num if item == NUM else self.__den

    def simplify(self):        
        divisor = gcd(self.__den, self.__num)
        self.__num //= divisor
        self.__den //= divisor
        return
    
# TEST
'''
r1 = Rational(1, 6)
r2 = Rational(2, 6)

print("1/6 + 2/6 =", r1 + r2)
print("1/6 - 2/6 =", r1 - r2)
print("1/6 * 2/6 =", r1 * r2)
print("1/6 / 2/6 =", r1 / r2)
print("is 1/6 < 2/6 :", r1 < r2)
print("is 1/6 <= 2/6 :", r1 <= r2)
print("is 1/6 = 2/6 :", r1 == r2)
print("is 1/6 not = 2/6 :", r1 != r2)
print("is 1/6 > 2/6 :", r1 > r2)
print("is 1/6 >= 2/6 :", r1 >= r2)
input("Press Enter to Continue")
'''
