def hex_digit(decimal):
    if decimal < 10:
        return chr(decimal + ord('0'))
    else:
        return chr((decimal-10) + ord('A'))
        
def convert(decimal):    
    if (decimal < 16):
        return hex_digit(decimal)
    else:
        quotient = decimal // 16
        remainder = decimal % 16
        return convert(quotient) + hex_digit(remainder)

def main():
    decimal = eval(input("Enter a number: "))
    hexadecimal = convert(decimal)
    print("The hexadecimal value for", decimal, "is", hexadecimal)

main()
input("Press Enter to continue...")

