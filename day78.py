'''For a given array B1?,B2?,…,BM? of length at least 3, let's define its weight as the largest value of (Bi?−Bj?)⋅(Bj?−Bk?) over all possible triples (i,j,k) with 1≤i,j,k≤M and i!=j, j!=k, k!=i.

You are given a sorted array A1?,A2?,…,AN? (that is, A1?≤A2?≤…≤AN?).

Calculate the sum of weights of all contiguous subarrays of A of length at least 3. That is, count the sum of weights of arrays [Ai?,Ai+1?,…,Aj?] over all 1≤i<j≤N with j−i≥2.

Input Format

The first line of input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains an integer N.
The second line of each test case contains N space-separated integers A1?,A2?,…,AN?.
Output Format

For each test case, print a single line containing the sum of weights of all subarrays of A of length at least 3.'''

for T in range(int(input())):
    N=int(input('Enter no of elements : '))
    A=list(map(int,(input('Enter the array elements : ').split())))
    total=0
    for i in range(N-2):
        j=i+1
        for k in range(i+2,N):
            mid = (A[i]+A[k])/2
            while(j < k-1) and (abs(A[j+1]- mid)<= abs(A[j]-mid)):
                j+=1
                total+=(A[j]-A[i])*(A[j]-A[k])
    print(abs(total))