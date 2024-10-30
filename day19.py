#Armstrong number or not
import math
num=int(input('Enter the number : '))
no_of_digits=int(math.log10(num)+1)   #find the number of digits of number (Can use len() function also)
sum=0
copy=num       #creating a copy of num to check atlast because value of number changes
for i in range (1,no_of_digits+1):   
    sum+=math.pow(num%10,no_of_digits)  #add each digit raised to the total number of digits
    num=num//10
if copy==sum:       
    print('Armstrong number')
else:
    print('Not an Armstrong number')