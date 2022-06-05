#Q15

str=input("Enter the string: ")
a=d=s=0
l=len(str)
for i in range(0,l):
    if str[i].isalpha():
        a+=1
    elif str[i].isdigit():
        d+=1
    else:
        s+=1   

print("No. of alphabets: ",a)
print("No. of digits: ",d)
print("No. of special characters: ",s)



