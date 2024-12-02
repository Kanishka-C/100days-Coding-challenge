#sum of positive square elements in array
size=int(input('Enter the size of array : '))
print('Enter the elements of the array : ')
arr=list(map(int,input().split()))
sum=0
for i in range(size):
    sum+=arr[i]*arr[i]
print('Sum of positive square elements in the array : ',sum)