#Smallest and largest element in array
size=int(input('Enter the size of array : '))
arr=[]
print('Enter the elements of array : ')
for i in range(size):
    arr.append(int(input()))
smallest=largest=arr[0]
for num in arr:
    if num<smallest:
        smallest=num
    elif num>largest:
        largest=num
print('Smallest number : ',smallest,'Largest number : ',largest)