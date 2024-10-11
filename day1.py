print('Welcome to Talent Battle')

c=input('enter a character')
if c in ('a','e','i','o','u','A','E','I','O','U'):
    print('Vowel')
elif c.isalpha():
    print("Consonant")
else:
    print("Invalid input")