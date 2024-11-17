#Character frequency of string
string=input('Enter a string : ')
freq={}
for x in string:
    freq[x]=string.count(x)
for key,value in freq.items():
    print('The frequency of ',key,' is ',value)