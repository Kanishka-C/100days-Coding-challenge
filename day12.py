#Sum of digits of a number
num=int(input("Enter the number : "))
sum=0
while num>0:
    sum+=num%10
    num=num//10
print("Sum is : ",sum)