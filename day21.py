#Palindrome number or not
num=input("Enter the number : ")
if num == num[::-1]:     #num[::-1] displays the string in reverse order
    print('Palindrome')  
else:
    print('Not a Palindrome')