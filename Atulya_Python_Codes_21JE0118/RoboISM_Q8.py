#Q8

str=input("Enter the string: ")
s=0
for i in range(len(str)):
    if ord(str[i])>=ord("0") and ord(str[i])<=ord("9"):
        s=s+int(str[i])
    

print(s)

