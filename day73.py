'''A string is called boring if all the characters of the string are same.
You are given a string S of length N, consisting of lowercase english alphabets. 
Find the length of the longest boring substring of S which occurs more than once.
Note that if there is no boring substring which occurs more than once in S, the answer will be 00.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two lines of input.
The first line of each test case contains an integer N, denoting the length of string S.
The next contains string S.

Output Format
For each test case, output on a new line, the length of the longest boring substring of S which occurs more than once.'''

T=int(input('Enter the number of test cases: '))
for _ in range(T):
    N=int(input('Enter the length of string : '))
    S=input('Enter the string : ')
    maxlen=0
    i=0
    dic={}
    while i<N:
        cnt=1
        substr=S[i]
        while i!=N-1 and S[i]==S[i+1] :
            cnt+=1
            i+=1
            substr+=S[i]
        maxlen=max(maxlen,cnt-1)
        dic[substr]=dic.get(substr,0)+1
        if dic[substr]>1:
            maxlen=max(maxlen,len(substr))
        i+=1
    print(maxlen)