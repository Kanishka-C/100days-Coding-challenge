#Check for anagrams
string1,string2=map(str,(input('Enter two strings : ')).split())
if sorted(string1)==sorted(string2):
    print('Anagram')
else:
    print('Not anagrams')