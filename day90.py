'''Gru has a string S of length N, consisting of only characters a and b for banana and P points to spend.
Now Gru wants to replace and/or re-arrange characters of this given string to get the lexicographically smallest string possible. 
For this, he can perform the following two operations any number of times.
Swap any two characters in the string. This operation costs 1 point. (any two, need not be adjacent)
Replace a character in the string with any other lower case english letter. This operation costs 2 points.
Help Gru in obtaining the lexicographically smallest string possible, by using at most P points.

Input:
First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains two lines of input, first-line containing two integers N , P.
The second line contains a string S consisting of N characters.

Output: For each testcase, output in a single containing the lexicographically smallest string obtained.'''
t = int(input())  # Number of test cases
for _ in range(t):
    n,p=map(int,(input().split()))
    s=list(input())
    swaps_needed=0
    sorted_s=sorted(s)
    for i in range(n):
        if s[i]!=sorted_s[i]:
            swaps_needed+=1
    swaps_needed//=2
    if swaps_needed<=p:
        p-=swaps_needed
        s=sorted_s
    for i in range(n):
        #if p
        if s[i]!='a' and p>=2:
            s[i]='a'
            p-=2
    print(''.join(s))