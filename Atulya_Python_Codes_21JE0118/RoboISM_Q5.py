#Q5

import random
def dup(list1):
    for i in list1:
        if((list1.count(list1[i]))>1):
            return(list1[i])

randomlist=[]
for x in range(1,99):
      n=random.randint(1,99)
      randomlist.append(n)
print("The duplicate element is: ",dup(randomlist))