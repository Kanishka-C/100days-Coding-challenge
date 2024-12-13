'''Anusree has decided to go to a gold mine along with N of his friends (thus, total N+1 people including Anusree go to the gold mine).
The gold mine contains a total of X kg of gold. Every person has the capacity of carrying up atmost Y kg of gold.
Will Anusree and his friends together be able to carry up all the gold from the gold mine assuming that they can go to the mine exactly once.

Input Format
First line will contain T, number of testcases. Then the testcases follow. Each testcase contains of a single line of input, three integers N, X, Y.

Output Format
For each testcase, output "YES" if you and your friends can carry all the gold, otherwise output "NO".'''

T=int(input('Enter the number of testcases : '))
for i in range(T):
    N,X,Y=map(int,(input('Enter the values of N,X,Y : ').split()))
    if X/(N+1)<=Y:
        print('YES')
    else:
        print('NO')