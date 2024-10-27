def fact(n):
    f=1
    for i in range (1,n+1):
        f=f*i
    return f
num=int(input("Enter a number : "))
sum=0
temp=num
if num==0:
    sum+=1      #Since 0!=1
while(num!=0):
    sum+=fact(num%10)
    num=num//10
if temp==sum:
    print("Strong number")
else:
    print('Not a strong number')