#Q1

def order(list1,type_order):
    if type_order=='asc':
        list1.sort()
        print(list1)
    elif type_order=='desc':
        list1.sort(reverse=True)
        print(list1)
    else:
        print(list1)


list1 = []
n= int(input("Enter number of elements : "))
print("Enter the elements :")
for i in range(1, n+1):
    element = int(input())
    list1.append(element)
      
order_type =input("Enter the type of order: ")
order(list1,order_type)

