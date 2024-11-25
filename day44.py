#Number of even and odd elements in array
size=int(input('Enter the size of array : '))
arr=[]
print('Enter the elements of array : ')
for i in range(size):
    arr.append(int(input()))
oddcnt,evencnt,zerocnt=0,0,0
for num in arr:
    if num==0:
        zerocnt+=1
    elif num%2==1:
        oddcnt+=1
    else:
        evencnt+=1
print('Number of even elements : ',evencnt)
print('Number of odd elements : ',oddcnt)
print('Number of zeros : ',zerocnt)