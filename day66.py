'''Anoop likes strings a lot but he likes palindromic strings more. 
Today, Anoop has two strings A and B, each consisting of lower case alphabets.
Anoop is eager to know whether it is possible to choose some non empty strings s1 and s2 where s1 is a substring of A, s2 is a substring of B such that s1 + s2 is a palindromic string.'''

T=int(input('Enter the number of testcases : '))
for i in range(T):
    A,B=map(str,(input('Enter two strings s1 and s2 : ').split()))
    flag=0
    for x in A:
        if x in B:
            print('Yes')
            flag=1
            break
    if flag==0:
        print('No')