def dfs(n,visited,computers):
    stack=[n]
    chk=0
    while stack:
        x=stack.pop()
        if x not in visited:
            visited.append(x)
            chk=1
            for i in range(len(computers[n])):
                if computers[x][i]==1 and x!=i:
                    stack.append(i)
    return chk

def solution(n, computers):
    visited=[]
    cnt=0
    for i in range(len(computers)):
        chk=dfs(i,visited,computers)
        if chk==1:
            cnt+=1
    return cnt
