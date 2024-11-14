#Palindrome string 
string=input('Enter a string : ')
if string[::-1] == string:
    print('Palindrome string')
else:
    print('Not a palindrome string')