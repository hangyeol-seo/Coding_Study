from collections import deque
import sys
read = sys.stdin.readline

v=int(input())
tree=[0]*(v+1)

def bfs(x):
    q=deque()
    q.append(x)
    visited=[0]*(v+1)
    visited[x]=1
    distance = [0]*(v+1)
    while q:
        n=q.popleft()
        for z in tree[n]:
            if visited[z]==0:
                visited[z]=1
                q.append(z)
                distance[z]=distance[n]+tree[n][z]
    max_distance = max(distance)
    max_node = distance.index(max_distance)
    return max_node,max_distance
            
for _ in range(v):
    length={}
    x=read().split()
    y=x[1:-1]
    for i in range(0,len(y),2):
        length[int(y[i])]=int(y[i+1])
    tree[int(x[0])]=length
    
node,distance=bfs(1)
max_node, max_distance = bfs(node)
print(max_distance)
