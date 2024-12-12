'''Given the time control of a chess match as a+b,determine which format of chess out of the given 4 it belongs to.
1) Bullet if a+b<3
2) Blitz if 3≤a+b≤10
3) Rapid if 11≤a+b≤60
4) Classical if 60<a+b

Input Format
First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains a single line of input, two integers a,b

Output Format
For each testcase, output in a single line, answer 1 for bullet, 2 for blitz, 3 for rapid, and 4 for classical format.'''

T=int(input('Enter the number of testcases : '))
for i in range(T):
    a,b=map(int,(input('Enter the values of a and b : ').split()))
    time_control=a+b
    if time_control<3:
        print('1 (Bullet)')
    elif time_control<=10:
        print('2 (Blitz)')
    elif time_control<=60:
        print('3 (Rapid)')
    else:
        print('4 (Classical)')