#Whether the numbers of an array be made equal
size=int(input('Enter the size of the array : '))
arr=list(map(int,input().split()))
for i in range (size):
    while arr[i]%2==0:
        arr[i]/=2
    while arr[i]%3==0:
        arr[i]/=3
    if arr[i]!=arr[0]:
        print('No')
        exit(0)
print('Yes')