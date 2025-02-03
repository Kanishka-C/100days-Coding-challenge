'''There are N stones in a pond, each having a value Ai? written on it. A frog is at stone 1 and wants to reach stone N. 
The frog can jump from a stone i to any stone j(j>i). Let d be the length of subarray (i.e. j−i+1), then the energy required for the jump is (d⋅Ai?)−Aj?. 
Find the minimum non-negative amount of energy required by the frog to reach the N-th stone.
Note: It is possible that the total amount of energy required is negative, in that case, you should print the minimum non-negative value (i.e. 0).

Input Format
The first line contains an integer T - the number of test cases. Then the test cases follow.
The first line of each test case contains an integer N - the number of stones.
The second line contains N integers denoting the numbers written on the stones.

Output Format
For each test case output a single integer - the minimum non-negative energy required by the frog.'''
T=int(input('Enter no of testcases : '))
for _ in range(T):
    N=int(input('Enter no of stones : '))
    st=list(map(int,input().split()))
    i,j=0,0
    stones=0
    while j<N:
        if st[j]>=st[i]:
            j+=1
        else:
            stones+=(j-i+1)*st[i]-st[j]
            i=j
    stones+=(N-i)*st[i]-st[N-1]
    if stones<0:
        print(0)
    else:
        print(stones)
