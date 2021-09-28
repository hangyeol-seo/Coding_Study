import sys
from collections import deque
read=sys.stdin.readline
def bfs(v,bg):
    q=deque()
    q.append(v)
    while q:
        v=q.popleft()
        color=visit_list[v]
        for i in graph[v]:
            if visit_list[i]==0:
                if color==1:
                    visit_list[i]=2
                else:
                    visit_list[i]=1
                q.append(i)
            elif visit_list[i]==color:
                print("NO")
                bg[0]=0
                break
        if bg[0]==0:
            break
            
k=int(input())
for i in range(k):
    n,m=map(int,read().split())
    visit_list=[0]*(n+1)
    graph={}
    for i in range(1,n+1):
        graph[i]=[]
    for i in range(m):
        a,b=map(int,read().split())
        graph[a].append(b)
        graph[b].append(a)
    bg=[1]
    for i in range(1,n+1):
        if visit_list[i]==0:
            bfs(i,bg)
    if bg[0]==1:
        print("YES")
