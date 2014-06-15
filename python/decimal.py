def intval(hex_digit):
    if str.isdigit(hex_digit):
        return int(hex_digit)
    else:
        return ord(hex_digit)-ord('A')+10

def convert(hexadecimal):
    hexadecimal = hexadecimal.upper()
    decimal = 0
    
    for i in range(len(hexadecimal)):
        last_index = len(hexadecimal)-1
        decimal += intval(hexadecimal[last_index-i]) * 16**i # right to left
        
    return decimal

def main():
    hexadecimal = input("Enter a hexadecimal number: ")
    decimal = convert(hexadecimal)
    print("The decimal value for", hexadecimal, "is", decimal)

main()
input("Press Enter to continue...")
