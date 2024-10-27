#Factors of a number
import math
num=int(input('Enter the number : '))
i=1
while i<=math.sqrt(num):
    if num%i==0:
        print(i,',',end='',sep='')
        if num//i!=i:
            print(num//i,',',end='',sep='')
    i+=1