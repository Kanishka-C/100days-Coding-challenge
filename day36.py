#First and last characters to uppercase
string = input('Enter a string : ')
newstr=string[0].upper()+string[1:-1]+string[-1].upper()
print(newstr)