#Array sorting
size=int(input('Enter the size of array : '))
print('Enter the elements of the array : ')
arr=list(map(int,input().split()))
for i in range(size-1):
    for j in range(size-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)