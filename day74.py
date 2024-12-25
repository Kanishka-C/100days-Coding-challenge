'''You have a grid with N rows and M columns. You have two types of tiles — one of dimensions 2×2 and the other of dimensions 1×1.
You want to cover the grid using these two types of tiles in such a way that:
Each cell of the grid is covered by exactly one tile; and
The number of 1×1 tiles used is minimized.
Find the minimum number of 1×1 tiles you have to use to fill the grid.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single line containing two space-separated integers N,M.

Output Format
For each test case, print on a new line the minimum number of 1×1 tiles needed to fill the grid.'''

T=int(input('Enter the number of test cases: '))
for _ in range(T):
    N,M=map(int,(input('Enter grid dimensions : ').split()))
    #find the no of rows and cols left after filling 2x2 tiles
    rows_left,cols_left=N%2,M%2
    if rows_left==0 and cols_left==0:
        tiles=0
    elif cols_left==0 and rows_left!=0:  #if no cols and 1 row left
        tiles=M  #1 row means M columns will be left hence M 1x1 tiles
    else:
        tiles=N   #1 column means N rowa will be left hence N 1x1 tiles
    print('No of 1x1 tiles needed =',tiles)