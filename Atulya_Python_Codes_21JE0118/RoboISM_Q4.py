#Q4

def string_rep(str):
    newStr=""
    l=len(str)
    for i in range(0,l):
        newStr  =newStr + (str[i]*2)
    return newStr

s=input("Enter a string: ")
print(string_rep(s))