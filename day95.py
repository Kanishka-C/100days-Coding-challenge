'''Kulyash is given an integer N. His task is to break N into some number of (integer) powers of 2.
To achieve this, he can perform the following operation several times (possibly, zero):
Choose an integer X which he already has, and break X into 2 integer parts (Y and Z) such that X=Y+Z.
Find the minimum number of operations required by Kulyash to accomplish his task.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single line of input.
The first and only line of each test case contains an integer N — the original integer with Kulyash.

Output Format
For each test case, output on a new line the minimum number of operations required by Kulyash to break N into powers of 2.

Sample Input
2
3
4

Sample Output
1
0'''
for _ in range(int(input())):
    N=int(input())
    print(bin(N).count('1')-1)  #Eg :N = 7 → Binary: 111 → Needs three powers of 2 (1, 2, 4) → 2 operations.