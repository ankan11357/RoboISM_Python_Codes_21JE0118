#Q11

def Palindrome(input_str):
    rev_str=''.join(reversed(input_str))
    if rev_str==input_str:
        print("Palindrome")
    else:
        print("Not a Palindrome")

s=input("Enter a String: ")
Palindrome(s)