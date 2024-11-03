n=int(input('Enter a number : '))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end='')
    for j in range(0,2*i+1):
        print("*",end='')
    for j in range(0,n-i-1):
        print(" ",end='')
    print('')