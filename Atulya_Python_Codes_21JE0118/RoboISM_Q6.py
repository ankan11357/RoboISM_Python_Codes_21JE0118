#Q6
def prime_num(m,n):
    c=0
    for i in range(m,n+1):
        for j in range(2,i+1):
            if i%j==0:
             c+=1
        if c==1:
         print(i)
        c=0

m=int(input("Enter the lower limit of the range: "))
n=int(input("Enter the upper limit of the range: "))            
print("Prime Numbers are: ")
prime_num(m,n)        
    