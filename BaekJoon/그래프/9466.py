import sys
sys.setrecursionlimit(10**8)
read = sys.stdin.readline
def dfs(x):
    global result
    visited[x]=True
    route.append(x)
    next = select_list[x]
    if not visited[next]:
        dfs(next)
    else:
        if next in route:
            position=route.index(next)
            result+=route[position:]
            return
T=int(input())
for _ in range(T):
    n=int(read())
    select_list=[0]+list(map(int,read().split()))
    result=[]
    visited=[True]+[False]*n
    for i in range(1,n+1):
        if not visited[i]:
            route=[]
            dfs(i)
    print(n-len(result))
