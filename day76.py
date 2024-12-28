'''You are given N integers. In each step you can choose some K of the remaining numbers and delete them, if the following condition holds: 
Let the K numbers you've chosen be a1, a2, a3, ..., aK in sorted order. 
Then, for each i ≤ K - 1, ai+1 must be greater than or equal to ai * C.
You are asked to calculate the maximum number of steps you can possibly make.

Input
The first line of the input contains an integer T, denoting the number of test cases. The description of each testcase follows.
The first line of each testcase contains three integers: N, K, and C
The second line of each testcase contains the N initial numbers

Output
For each test case output the answer in a new line.'''

T=int(input('Enter the number of test cases: '))
for _ in range(T):
    N,K,C=map(int,(input('Enter N,K,C : ').split()))
    numbers=list(map(int,(input('Enter the numbers : ').split())))
    numbers.sort()
    step=0
    while(len(numbers)>=K):
        index=1
        group=[numbers[0]]
        while index<len(numbers) and len(group)<=K:
            if group[-1]*C <= numbers[index]:
                group.append(numbers[index])
            index+=1
        if len(group)==K:
            step+=1
            for n in group:
                numbers.remove(n)
        else:
            break
    print(step)