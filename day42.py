#Two arrays are same or not
n1=int(input('Enter the size of first array : '))
n2=int(input('Enter the size of second array : '))
arr1=[]
arr2=[]
print('Enter elements of first array :')
for i in range (n1):
    arr1.append(int(input()))
print('Enter elements of second array :')
for i in range(n2):
    arr2.append(int(input()))
arr1.sort()
arr2.sort()
if arr1==arr2:
    print('Same')
else:
    print('Different')