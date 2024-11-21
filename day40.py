#Replace substring in a string
string=input('Enter a string : ')
remove_substring=input('Enter the substring to be removed : ')
if string.find(remove_substring)>0:
    new_substring=input('Enter the new substring : ')
    print('The new string : ',string.replace(remove_substring,new_substring))
else:
    print(remove_substring,' is not a part of ',string)