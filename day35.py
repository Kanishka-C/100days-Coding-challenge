#Sum of numbers in a string
string=input('Enter a string with numbers : ')
sum=0
for s in string:
    if s.isdigit():
        sum+=int(s)
print('Sum of digits : ',sum)