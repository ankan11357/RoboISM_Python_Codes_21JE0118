#Q7

def frequency(given_array):
    max_freq = 0
    x = 0
    for i in given_array:
        c = given_array.count(i) 
        if c>x:
            x=c
            max_freq = i
            
    print("Number with highest frequency is :",max_freq)


given_array = []
n = int(input("Enter number of elements : "))
print("Enter the elements :")
for i in range(1, n+1):
    element = int(input())
    given_array.append(element)
    
frequency(given_array)