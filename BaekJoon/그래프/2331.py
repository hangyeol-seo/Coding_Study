A,P=map(int,input().split())

def dfs(x,p):
    visited[x]=True
    numbers.append(x)
    number=str(x)
    num=0
    for i in number:
        num+=(int(i))**p
    if not visited[num]:
        dfs(num,p)
    else:
        result.append(num)
visited=[True]+[False]*((9**P)*4)
numbers=[]
result=[]
dfs(A,P)
position=numbers.index(result[0])
print(position)
