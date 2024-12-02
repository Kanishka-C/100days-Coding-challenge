#sum of positive square elements in array
print('Enter the elements of the array : ')
arr=list(map(int,input().split()))
unique_elements=set()
sum=0
for num in arr:
    num=abs(num)
    if num not in unique_elements:
        unique_elements.add(num)
        sum+=num*num
print('Sum of positive square elements in the array : ',sum)