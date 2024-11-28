#Array sum
size=int(input('Enter the size of array : '))
arr=[] 
#sums=0
print('Enter the elements of the array : ')
for i in range (size):
    arr.append(int(input()))
    #sums+=arr.pop()
print('Sum of elements=',sum(arr))
#print('Sum of elements=',sums)