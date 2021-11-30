from collections import deque
import numpy as np

def bfs(start,matrix,end):
    visited=set([start])
    queue=deque([start])
    distance={}
    distance[start]=0

    while queue:
        n=queue.popleft()
        if n==end:
            return distance[n]
        direc=[(n[0],n[1]+0.5),(n[0]+0.5,n[1]),(n[0],n[1]-0.5),(n[0]-0.5,n[1])]
        for i in direc:
            if i in matrix and i not in visited:
                queue.append(i)
                visited.add(i)
                distance[i]=distance[n]+0.5
    return 0

def solution(rectangle, characterX, characterY, itemX, itemY):
    border=set()
    inside=set()
    for rec in rectangle:
        lx,ly,rx,ry=rec
        for x in np.arange(lx,rx+0.1,0.5):
            for y in np.arange(ly,ry+0.1,0.5):
                if x==lx or x==rx or y==ly or y==ry:
                    if (x,y) not in inside and (x,y) not in border:
                        border.add((x,y))
                else:
                    if (x,y) in border:
                        border.remove((x,y))
                        inside.add((x,y))
                    else:
                        if (x,y) not in inside:
                            inside.add((x,y))
    now=(characterX,characterY)
    return bfs(now,border,(itemX,itemY))
