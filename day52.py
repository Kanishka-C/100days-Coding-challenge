#Array reversal
size=int(input('Enter the size of array : '))
print('Enter the elements of the array : ')
arr=list(map(int,input().split()))
rev=[]
for i in range(size-1,-1,-1):
    rev.append(arr[i])
#arr.reverse()
print('Reversed array : ',rev)