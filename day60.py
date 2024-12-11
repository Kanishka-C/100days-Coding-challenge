'''The weather report of Magicland is Good if the number of sunny days in a week is strictly greater than the number of rainy days.
Given 7 integers A1,A2,A3,A4,A5,A6,A7 where Ai=1 denotes that the ith day of week in Magicland is a sunny day, Ai=0 denotes that the ith day in Magicland is a rainy day. 
Determine if the weather report of Magicland is Good or not.

Input Format
First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains of a single line of input, 7 space separated integers A1,A2,A3,A4,A5,A6,A7.

Output Format
For each testcase, print "YES" if the weather report of Magicland is Good, otherwise print "NO".'''

T=int(input('Enter the number of testcases : '))
for i in range(T):
    A=list(map(int,(input('Enter A1 to A7 : ').split())))
    if len(A)!=7 or any(x not in (0,1) for x in A):
        print('Invalid input')
    elif A.count(1)>A.count(0):
        print('YES')
    else:
        print('NO')