import sys
read=sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x,li):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny <n:
            if matrix[ny][nx]==0:
                li.append((ny,nx))
                matrix[ny][nx]=1
                cnt+=1
                
m,n = map(int,input().split())
matrix = [[0]*m for _ in range(n)]
tomato=m*n
ripe=[]
for i in range(n):
    line = list(map(int,input().split()))
    for j, b in enumerate(line):
        matrix[i][j] = b
        if b==-1:
            tomato-=1
        elif b==1:
            ripe.append((i,j))
            
length=len(ripe)  
if length==tomato:
    print(0)
else:
    day=0
    cnt=length
    old=ripe.copy()
    new=[]
    while True:
        for a,b in old:
            dfs(a,b,new)     
        old=new.copy()
        new=[]
        day+=1
        if cnt==tomato:
            print(day)
            break
        elif len(old)==0:
            print(-1)
            break
