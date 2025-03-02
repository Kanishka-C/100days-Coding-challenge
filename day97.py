'''Arun has a rooted tree of N vertices rooted at vertex 1. Each vertex can either be coloured black or white.
Initially, the vertices are coloured A1?,A2?,…AN?, where Ai? ∈ {0,1} denotes the colour of the i-th vertex (here 0 represents white and 1 represents black). 
He wants to perform some operations to change the colouring of the vertices to B1?,B2?,…BN? respectively.

Arun can perform the following operation any number of times. In one operation, he can choose any subtree and either paint all its vertices white or all its vertices black.
Help Arun find the minimum number of operations required to change the colouring of the vertices to B1?,B2?,…BN? respectively.

Input Format
The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first line of each test case contains an integer N — the size of the tree.
The second line of each test case contains N space-separated integers A1?,A2?,…,AN? denoting the initial colouring of the vertices of the tree.
The third line of each test case contains N space-separated integers B1?,B2?,…,BN? denoting the final desired colouring of the vertices of the tree.
The next N−1 lines contain two space-separated integers u and v — denoting an undirected edge between nodes u and v.
It is guaranteed that the edges given in the input form a tree.

Output Format
For each testcase, output the minimum number of operations required to obtain the desired colouring.'''
def min_operations(n, A, B, edges):
    from collections import defaultdict
    
    # Step 1: Construct the tree using adjacency list
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Step 2: DFS to count necessary changes
    def dfs(node, parent):
        mismatch_white = mismatch_black = 0
        for child in tree[node]:
            if child == parent:
                continue
            child_white, child_black = dfs(child, node)
            mismatch_white += child_white
            mismatch_black += child_black
        
        # If A[node] != B[node], it's a mismatch
        if A[node] != B[node]:
            if B[node] == 0:
                mismatch_white += 1
            else:
                mismatch_black += 1

        # The number of operations needed is the max of required changes
        return mismatch_white, mismatch_black

    # Convert to zero-based index
    A = [a for a in A]
    B = [b for b in B]
    
    # Get the required number of operations
    white_ops, black_ops = dfs(1, -1)  # Start DFS from the root node (1)
    
    return max(white_ops, black_ops)

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    '''A = list(map(int, input().split()))
    B = list(map(int, input().split()))'''
    A = [0] + list(map(int, input().split()))  # Add a dummy value at index 0
    B = [0] + list(map(int, input().split()))  # Add a dummy value at index 0

    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    
    # Print the result
    print(min_operations(n, A, B, edges))
