'''You are given an array A of N elements. For any ordered triplet (i,j,k) such that i, j, and k are pairwise distinct and 1≤i,j,k≤N, the value of this triplet is (Ai?−Aj?)⋅Ak?. 
You need to find the maximum value among all possible ordered triplets.
Note: Two ordered triplets (a,b,c) and (d,e,f) are only equal when a=d and b=e and c=f. As an example, (1,2,3) and (2,3,1) are two different ordered triplets.

Input Format
The first line of the input contains a single integer T - the number of test cases. The test cases then follow.
The first line of each test case contains an integer N.
The second line of each test case contains N space-separated integers A1?,A2?,…,AN?.

Output Format
For each test case, output the maximum value among all different ordered triplets.'''

T=int(input('Enter the number of test cases: '))
for _ in range(T):
    N=int(input('Enter the no of elements : '))
    A=list(map(int,(input('Enter the numbers : ').split())))
    diff=max(A)-min(A)
    A.remove(max(A))
    print(diff*max(A))