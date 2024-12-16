'''Ajinkya decided to buy a new tablet. His budget is B, so he cannot buy a tablet whose price is greater than B. 
Other than that, he only has one criterion — the area of the tablet's screen should be as large as possible.
Ajinkya has visited some tablet shops and listed all of his options. 
In total, there are N available tablets, numbered 1 through N. 
For each valid i, the i-th tablet has width Wi, height Hi and price Pi.
Help Ajinkya choose a tablet which he should buy and find the area of such a tablet's screen, or determine that he cannot buy any tablet.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and B. N lines follow.
For each i (1≤i≤N), the i-th of these lines contains three space-separated integers Wi, Hi and Pi.

Output
For each test case, print a single line. If Ajinkya cannot buy any tablet, it should contain the string "no tablet".
Otherwise, it should contain a single integer — the maximum area of the screen of a tablet Ajinkya can buy.'''

T=int(input('Enter the number of testcases : '))
for i in range(T):
    N,B=map(int,(input('Enter N and budget : ').split()))
    max_screenarea=-1
    for j in range (N):
        W,H,P=map(int,(input('Enter width, height and price : ').split()))       
        screen_area=W*H
        if P<=B and screen_area>max_screenarea:
            max_screenarea=screen_area
    if max_screenarea==-1:
        print('No tablet')
    else:
        print(max_screenarea)