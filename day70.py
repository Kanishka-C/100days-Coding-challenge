#Given an array, rotate the array by one position in clock-wise direction.
n=int(input('Enter no of elements : '))
A=list(map(int,(input('Enter the array elements : ').split())))
A.insert(0,A.pop())
print(A)