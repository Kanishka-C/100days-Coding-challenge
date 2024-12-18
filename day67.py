'''Arunima stacked three bricks on top of each other. 
Initially, their widths (from top to bottom) are W1,W2,W3.Arunima strength is S. 
Whenever she hits a stack of bricks, consider the largest k≥0 such that the sum of widths of the topmost k bricks does not exceed S; the topmost k bricks break and are removed from the stack. 
Before each hit, Arunima may also decide to reverse the current stack of bricks, with no cost.
Find the minimum number of hits Arunima needs in order to break all bricks if she performs the reversals optimally. You are not required to minimize the number of reversals.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains four space-separated integers S, W1, W2 and W3.

Output
For each test case, print a single line containing one integer ? the minimum required number of hits'''

T = int(input('Enter the number of test cases: '))

for _ in range(T):
    S, W1, W2, W3 = map(int, input('Enter S and widths W1, W2, W3: ').split())

    # Function to calculate hits for a given stack
    def calculate_hits(stack):
        hits = flag = 0
        current_strength = 0
        for brick in stack:
            if current_strength + brick <= S:
                current_strength += brick
                flag=1
            else:
                hits += 1
                current_strength = brick
        if current_strength > 0 and flag==1:  # Add one final hit for remaining bricks
            hits += 1
        else:
            hits=0
        return hits

    # Calculate hits for both original and reversed stacks
    hits_original = calculate_hits([W1, W2, W3])
    hits_reversed = calculate_hits([W3, W2, W1])

    # Print the minimum hits
    print(min(hits_original, hits_reversed))
