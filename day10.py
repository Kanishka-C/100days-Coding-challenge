num=int(input('Enter a number : '))
f=1
if num<0:
    print('Invalid input')
else:
    for i in range(2,num+1):
       f=f*i
    print('Factorial of ',num,'is ',f)