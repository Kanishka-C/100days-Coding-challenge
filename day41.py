#Wildcard string and normal string match or not
def matches(str1,str2):
    n,m=len(str1),len(str2)
    if n==0 and m==0:
        return True
    if n>1 and str1[0] == '*' and m == 0:
        return False
    if (n > 1 and str1[0] == '?') or (n != 0 and m !=0 and str1[0] == str2[0]):
        return matches(str1[1:],str2[1:])
    if n !=0 and str1[0] == '*':
        return matches(str1[1:],str2) or matches(str1,str2[1:])
    return False
wdcard_string=input('Enter a string with wildcards (? or *) : ')
string=input('Enter the string to be compared : ')
if matches(wdcard_string,string):
    print('Yes they match')
else:
    print('No they dont match')