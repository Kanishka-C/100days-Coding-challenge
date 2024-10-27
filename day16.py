#Perfect number
import math
num=int(input('Enter the number : '))
sum,i=0,1
if num>1:
    while i<=int(math.sqrt(num)):
        if num%i==0:
            sum+=i
            if num//i!=i and num//i!=num:
                sum+=num//i
        i+=1
else:
    sum=-1
if(num==sum):
    print('Perfect number')
else:
    print('Not a perfect number')