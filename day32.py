#Vowel removal from a string
str1=input('Enter a string : ') 
remstr=''
for x in str1:
    if x not in ('a','e','i','o','u','A','E','I','O','U'):
        remstr+=x
print('String without vowels : ',remstr)