#Replace substring in a string
string=input('Enter a string : ')
remove_substring=input('Enter the substring to be removed : ')
new_substring=input('Enter the new substring : ')
index=string.find(remove_substring)
print('The new string : ',string.replace(remove_substring,new_substring))