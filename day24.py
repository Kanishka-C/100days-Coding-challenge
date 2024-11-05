'''  
   *   
  ***
 *****
*******
'''
n=int(input('Enter number of rows: '))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end='')
    for j in range(0,2*i+1):
        print("*",end='')
    for j in range(0,n-i-1):
        print(" ",end='')
    print('')