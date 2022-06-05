#Q3

def operation(x,y,op):
    if op=="+":
        return x+y
    elif op=="-":
        return x-y
    elif op=="/":
        return x/y
    elif op==".":
        return x*y
a=int(input("Enter the first number= "))
b=int(input("Enter the second number= "))
op=input("Enter the type of operation: ")
print(operation(a,b,op))