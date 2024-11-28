#Longest palindrome
size=int(input('Enter the size of array : '))
arr=[]
longest_length=0
longest_palindrome=''
print('Enter the elements of array : ')
for i in range(size):
    arr.append((input()))
    if str(arr[i])==''.join(reversed(str(arr[i]))) and len(arr[i])>longest_length:
        longest_palindrome=arr[i]
        longest_length=len(arr[i])
if longest_palindrome:
    print('Longest palindrome is : ',longest_palindrome)
else:
    print('No palindromes found')