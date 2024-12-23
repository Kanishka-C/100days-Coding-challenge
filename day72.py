'''An editor maintains the content of a string S and have two following functions:
"+ i x": insert a string x into the current string S after the i'th character of the S (we use 1-indexing in this problem). 
When i equals to 0 it mean we add x at the beginning of S.
"? i len": Print the sub-string of length len starting at position i'th of S.
At the beginning, the editor holds an empty string. There will be Q queries of the two types described above.

Input
The first line contains the integer Q. Each line in the next Q lines contains one query.

Output
For each query of the second type, print out the answer sub-string in one line.'''

Q=int(input('Enter the no of queries : '))
S=''
for _ in range(Q):
    sym,i,x=map(str,(input('Enter the query : ').split()))
    i=int(i)
    if sym=='+':
        if i==0:
            S=x+S
        else:
            before_index_part=S[:i]
            after_index_part=S[i:]
            S=before_index_part+x+after_index_part
    elif sym=='?':
        print(S[(i-1):int(x)+1])
    else:
        print('Invalid function')