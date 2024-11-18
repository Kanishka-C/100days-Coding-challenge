#Non-repeating characters in string
string=input('Enter a string : ')
flag=0
for x in string:
    if string.count(x)==1:
        print(x,end=' ')
        flag=1
if flag==0:
    print('All characters are repeating')