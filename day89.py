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
def max_steps(n, k, c, arr):
    arr.sort()  # Step 1: Sort the array
    steps = 0   # Count of valid steps
    used = [False] * n  # Track if a number is already used in a group

    i = 0  # Pointer to find valid groups
    while i < n:
        group = []  # Store elements forming a valid group
        for j in range(i, n):
            if not used[j]:  # Pick only unused elements
                if len(group) == 0 or arr[j] >= group[-1] * c:
                    group.append(arr[j])  # Add to the group
                    used[j] = True  # Mark as used
                    if len(group) == k:  # If we formed a valid group of K
                        steps += 1
                        break  # Move to the next group

        i += 1  # Move to the next element to start a new group

    return steps

# Read input
t = int(input())  # Number of test cases
for _ in range(t):
    n, k, c = map(int, input().split())  # Read N, K, C
    arr = list(map(int, input().split()))  # Read the N numbers
    print(max_steps(n, k, c, arr))  # Compute and print the result