#Arrays are disjoint or not
n1=int(input('Enter number of elements of first array : '))
print('Enter the array elements : ')
arr1=list(map(int,input().split()))
n2=int(input('Enter number of elements of second array : '))
print('Enter the array elements : ')
arr2=list(map(int,input().split()))
for num in arr1:
    if num in arr2:
        print('Not disjoint ',num,' is common')
        exit(0)
print('Disjoint')