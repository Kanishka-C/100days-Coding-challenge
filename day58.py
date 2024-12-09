'''Nejiya has a bucket having a capacity of K liters. It is already filled with X liters of water.
Find the maximum amount of extra water in liters that Nejiya can fill in the bucket without overflowing.

Input Format
The first line will contain T - the number of test cases. Then the test cases follow.
The first and only line of each test case contains two space separated integers K and X - as mentioned in the problem.

Output Format
For each test case, output in a single line, the amount of extra water in liters that Nejiya can fill in the bucket without overflowing.'''

T=int(input('Enter the number of testcases : '))
for i in range (T):
    K,X=map(int,(input('Enter the values of K and X : ').split()))
    print('Amount of water that can be filled without overflowing : ',K-X)