#Minimum scalar product of 2 vector arrays
size=int(input('Enter the size of array : '))
print('Enter the elements of array x : ')
x=list(map(int,input().split()))
print('Enter the elements of array y : ')
y=list(map(int,input().split()))
product=0
x.sort()
y.sort(reverse=True)
for i in range(size):
    product+=x[i]*y[i]
print("Minimum scalar product is : ",product)