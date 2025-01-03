'''Alice and Bob went to a pet store. There are N animals in the store where the ith animal is of type Ai?.
Alice decides to buy some of these N animals. Bob decides that he will buy all the animals left in the store after Alice has made the purchase.
Find out whether it is possible that Alice and Bob end up with exactly same multiset of animals.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains an integer N — the number of animals in the store.
The next line contains N space separated integers, denoting the type of each animal.

Output Format
For each test case, output on a new line, YES, if it is possible that Alice and Bob end up with exactly same multiset of animals and NO otherwise.'''

from collections import Counter
T = int(input("Enter the number of test cases: "))
for _ in range(T):
    n=int(input('Enter N : '))
    A=list(map(int,(input('Enter the array elements : ').split())))
    arr=Counter(A)
    possible = True
    for i in arr:
        if arr[i]%2==1:
            possible=False
    if possible:
        print('YES')
    else:
        print('NO')