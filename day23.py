#Replace all 0's with 1 in a string
num=list(input('Enter a number : '))
for i in range (len(num)):
    if num[i]=='0':
        num[i]='1'
print(''.join(num))