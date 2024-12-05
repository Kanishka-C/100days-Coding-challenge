#Maximum product subarray
n=int(input('Enter the size of the array : '))
print('Enter the elements of the array : ')
arr=list(map(int,input().split()))
maximumProd=1
forward=1  #from left to right
backward=1  #from right to left
start=end=0
temp_start=0
for i in range (n):
    if forward==0:       #if encountered a zero, reset the product back to 1
        forward=1
        temp_start=i+1
    forward*=arr[i]
    if forward>maximumProd:
        maximumProd=forward
        start,end=temp_start,i
    if backward==0:
        backward=1
    backward*=arr[n-i-1]
    if backward>maximumProd:
        maximumProd=backward
        start,end=n-i-1,n-1
print('Maximum product sub array is : ',maximumProd,' = ',arr[start:end+1])