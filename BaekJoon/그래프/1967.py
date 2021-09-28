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
        if tree[n]!=0:
            for z in tree[n]:
                if visited[z]==0:
                    visited[z]=1
                    q.append(z)
                    distance[z]=distance[n]+tree[n][z]
    max_distance = max(distance)
    max_node = distance.index(max_distance)
    return max_node,max_distance
            
for _ in range(v-1):
    a,b,c=map(int,read().split())
    if tree[a]==0 :
        tree[a]={b:c}
    else:
        tree[a][b]=c
    if tree[b]==0:
        tree[b]={a:c}
    else:
        tree[b][a]=c
        
node,distance=bfs(1)
max_node, max_distance = bfs(node)
print(max_distance)
