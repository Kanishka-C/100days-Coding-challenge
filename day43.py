#Array type(odd/even/mixed)
def arraytype(array,n):
    oddcnt,evencnt=0,0
    for num in array:
        if num%2==0:
            evencnt+=1
        else:
            oddcnt+=1
    if evencnt==n:
        return "Even"
    elif oddcnt==n:
        return "Odd"
    else:
        return "Mixed"
size=int(input('Enter the size of array : '))
arr=[]
print('Enter the elements of array : ')
for i in range(size):
    arr.append(int(input()))
print(arraytype(arr,size))