#Prime number or not
import math
num=int(input('Enter the number : '))
count=0
for i in range(1,int(math.sqrt(num))+1):
    if num%i==0:
        count+=1
        if((num//i)!=i):
            count+=1
if count==2:
    print("Prime number")
else:
    print("Not a prime number")