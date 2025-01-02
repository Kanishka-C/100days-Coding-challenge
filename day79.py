'''You are given a binary string S of length N.
Flip the values of set of picked indices such that no two indices are adjacent.
Find the minimum number of operations required to convert all the characters of S to 0.

Input Format
The first line contains a single integer T - the number of test cases. Then the test cases follow.
The first line of each test case contains an integer N - the length of the binary string S.
The second line of each test case contains a binary string S of length N.

Output Format
For each test case, output the minimum number of operations required to convert all the characters of S to 0.'''

T = int(input("Enter the number of test cases: "))
for _ in range(T):
    N = int(input("Enter the length of the binary string S: "))
    S = input("Enter the binary string S: ")
    count = 0
    i = 0  
    while i < N:
        if S[i] == '1':
            count += 1  # Perform a flip operation at this index
            while i<N and S[i]=='1':
                i += 2  # Skip the next index to ensure non-adjacency
            while i<N and S[i]!=1:
                i+=1
        else:
            i += 1  # Move to the next index
    if S.count('1')==N:
        count=2
    print(count)
