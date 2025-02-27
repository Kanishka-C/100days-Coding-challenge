'''Kekocity's population consist of N gnomes numbered with unique ids from 1 to N. It takes exactly one minute to read and resend joke to mates.
You will be given a list of friends for every gnome and M queries of the following type: Who will receive a message with joke after exactly K minutes, if the creator of joke was gnome with id x?

Input
The first line contains a single integer N denoting the number of gnomes.
The next N lines contain the the matrix g[N][N]. Each of the i-th line, will contain N space separated integers - j-th of those will denote g[i][j]. If gnome j is friend of gnome i, then g[i][j] is 1. Otherwise it will be zero. 
Plese note that the friendship relationship is not bidirectional, i.e. it might happen that g[i][j] may not be equal to g[j][i]. Also one can be friend of itself also, i.e. g[i][i] may be equal to 1.
The next line contains a single integer M denoting the number of queries. The next M lines contain two integers k and x described above.

Output
For each query, output two lines.
In the first line, output how many gnomes will know the joke after k minutes.
In the second line, print these ids (numbering) of these gnomes in increasing order. If no one will know the joke after K minutes, then print -1 in this line.'''
from collections import deque
def bfs(graph,n,start,k):
    queue=deque([(start,0)])
    visited={}
    while queue:
        gnome,time=queue.popleft()
        if time>k:
            break
        if gnome not in visited:
            visited[gnome]=time
        for friend in range(1,n+1):
            if graph[gnome][friend]==1 and friend not in visited:
                queue.append((friend,time+1))
    result=sorted([gnome for gnome,time in visited.items() if time==k])
    return result
n=int(input('Enter no of gnomes : '))
print('Enter the friendship matrix : ')
g=[[0]*(n+1)]
for i in range(n):
    row=list(map(int,input('Enter row '+str(i+1)+':').split()))
    g.append([0]+row)
m=int(input('Enter no of queries : '))
for _ in range(m):
    k,x=map(int,input('Enter k and x : ').split())
    r=bfs(g,n,x,k)   
    if r:
        print(len(r))
        print(' '.join(map(str,r)))
    else:
        print(0)
        print(-1)
'''import numpy as np 
 
def getPowers(x): 
  k = 2 
  ret = [x] 
  done = False 
  while k < 10**9: 
    if done: 
      ret += [x] 
    else: 
      y = x.dot(x) 
      y[y>0] = 1 
      done = np.all(y==x) 
      x = y 
      ret += [x] 
    k *= 2 

  return ret 
                                                                                                                                   
def mpow(xp,z,k):  
    i = 0 
    while k > 0: 
        if k%2 == 1: 
            z = xp[i].dot(z) 
        i = i+1 
        k //= 2 
    return z 
def solve(x,y): 
    xp = getPowers(x) 
    n = x.shape[0] 
    for k,z in y: 
        z0 = np.zeros(n) 
        z0[z]=1 
        z0 = mpow(xp,z0,k) 
        ret = list(np.where(z0>0)[0]) 
        print(len(ret)) 
        if len(ret)==0: 
            print(-1) 
        else: 
            print(" ".join(str(x+1) for x in ret)) 
import sys 
f = sys.stdin 
n = int(f.readline())                                                                                                                                           
x = []    
for j in range(n): 
    y = list(map(int,f.readline().split())) 
    x += [y] 
x = np.array(x,dtype=np.float64).transpose()     
m = int(f.readline()) 
y = [] 
for i in range(m): 
    a,b = map(int,f.readline().split()) 
    y += [(a,b-1)] 
solve(x,y) '''
