import sys
from collections import deque
read=sys.stdin.readline
def bfs(v):
    q=deque()
    q.append(v)
    while q:
        v=q.popleft()
        for i in range(1,n+1):
            if visit_list[i]==0 and graph[v][i]==1:
                visit_list[i]=1
                q.append(i)
            
n,m=map(int,read().split())
visit_list=[0]*(n+1)
graph=[[0]*(n+1) for i in range(n+1)]
for i in range(m):
    a,b=map(int,read().split())
    graph[a][b]=graph[b][a]=1

cc=0

for i in range(1,n+1):
    if visit_list[i]==0:
        bfs(i)
        cc+=1
print(cc)
