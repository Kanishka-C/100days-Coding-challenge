'''Given an undirected graph and an integer M. 
The task is to determine if the graph can be colored with at most M colors such that no two adjacent vertices of the graph are colored with the same color. 
Here coloring of a graph means the assignment of colors to all vertices. Print 1 if it is possible to colour vertices and 0 otherwise.

Example 1:
Input:
N = 4
M = 3
E = 5
Edges[] = {(0,1),(1,2),(2,3),(3,0),(0,2)}
Output: 1
Explanation: It is possible to colour the given graph using 3 colours.'''

def graphcolor(graph,m,i,colors):
    if i==n:
        for j in range(n):
            for k in range(j+1,n):
                if graph[j][k]==1 and colors[j]==colors[k]:
                    return False
        print('1')
        return True
    for j in range(1,m+1):
        colors[i]=j
        if graphcolor(graph,m,i+1,colors):
            return True
        colors[i]=0
    return False
n=int(input('Enter no of nodes : '))
m=int(input('Enter no of colors : '))
e=int(input('Enter no of edges : '))
print('Enter the edges as ordered pair of end vertices : ')
graph=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(0)
    graph.append(a)
for _ in range(e):
    x,y=map(int,(input('Enter the edge : ').split()))
    graph[x][y]=1
    graph[y][x]=1
colors=[0]*5
if (not graphcolor(graph,m,0,colors)):  
    print('0')        