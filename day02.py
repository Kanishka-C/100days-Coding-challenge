print("Enter a character : ")
c=input()
if(c<='z' and c>='a') or (c<='Z' and c>='A'):  #or c.isalpha()
    print("Alphabet")
else:
    print("Not an alphabet")