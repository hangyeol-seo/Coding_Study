dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(start,matrix):
    visited=set([start])
    stack=[start]
    while stack:
        n=stack.pop()
        for nx,ny in zip(dx,dy):
            next=(n[0]+nx,n[1]+ny)
            if 0<=next[0]<=4 and 0<=next[1]<=4 and abs(start[0]-next[0])+abs(start[1]-next[1])<=2:
                if next not in visited and matrix[next[1]][next[0]]!='X':
                    if matrix[next[1]][next[0]]=='P':
                        return 0
                    else:
                        visited.add(next)
                        stack.append(next)
    return 1

def solution(places):
    answer=[]
    for i,place in enumerate(places):
        result=1
        for j,row in enumerate(place):
            for k,r in enumerate(row):
                if r=='P':
                    result=dfs((k,j),places[i])
                if result==0:
                    break
            if result==0:
                break
        if result==0:
            answer.append(0)
        else:
            answer.append(1)
    return answer
