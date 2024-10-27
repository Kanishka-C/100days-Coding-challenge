n=int(input('Enter the num : '))
first=0
second=1
print('Fibonacci series : ',first,',',second,end='',sep='')
for i in range (3,n+1):    
    third=first+second
    print(',',third,end='',sep='')
    first=second
    second=third