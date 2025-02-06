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
