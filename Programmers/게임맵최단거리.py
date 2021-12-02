from collections import deque
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(start,end,matrix):
    dist={}
    visited=set([start])
    queue=deque([start])
    dist[start]=1
    while queue:
        n=queue.popleft()
        if n==end:
            return dist[n]
        for x,y in zip(dx,dy):
            next=(n[0]+x,n[1]+y)
            if 0<=next[0]<=end[0] and 0<=next[1]<=end[1] and matrix[next[1]][next[0]]==1 and next not in visited:
                visited.add(next)
                queue.append(next)
                dist[next]=dist[n]+1
    return -1
def solution(maps):
    return bfs((0,0),(len(maps[0])-1,len(maps)-1),maps)
