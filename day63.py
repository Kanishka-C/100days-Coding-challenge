'''Manish's weight before the lockdown was w1 kg (measured on the most accurate hospital machine) and after M months of lockdown, 
when he measured his weight at home (on a regular scale, which can be inaccurate), he got the result that his weight was w2 kg (w2>w1).

Scientific research in all growing kids shows that their weights increase by a value between x1 and x2 kg (inclusive) per month, but not necessarily the same value each month. 
Manish assumes that he is a growing kid. Tell him whether his home scale could be giving correct results.

Input
The first line of the input contains a single integer T denoting the number of test cases. 
The description of T test cases follows. The first and only line of each test case contains five space-separated integers w1, w2, x1, x2 and M.

Output
For each test case, print a single line containing the integer 1 if the result shown by the scale can be correct or 0 if it cannot.'''

T=int(input('Enter the number of testcases : '))
for i in range(T):
    w1,w2,x1,x2,M=map(int,(input('Enter the values of w1,w2,x1,x2 and M : ').split()))
    if w2>w1:
        minWeight=w1+M*x1
        maxWeight=w2+M*x2
        if w2>=minWeight and w2<=maxWeight:
            print(1)
        else:
            print(0)