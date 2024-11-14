#Expression without brackets ()
string=input('Enter an algebraic expression : ')
newexp=''
for x in string:
    if x not in ('(',')'):
        newexp+=x
print(newexp)