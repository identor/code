def ispalindrome(string):
    last = len(string)-1 # The last index of string
    
    for i in range(len(string)):
        if string[i] != string[last]:
            return False
        last -= 1
        if last == i:
            break
        
    return True

def main():
    s = input("Enter a palindrome: ")
    print(("Yes, " + s + " is a palindrome") if ispalindrome(s) \
          else (s + " is not a palindrome"))
    
main()
input("Press Enter to continue...")
