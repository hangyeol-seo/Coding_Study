import sys
read=sys.stdin.readline
sys.setrecursionlimit(10**8)
dx = [-1,-1,-1, 0, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1,0,1,-1,0,1]

def dfs(x, y):
    visited[y][x] = 1  
    global nums           
    if matrix[y][x] == 1:
        nums += 1
    for i in range(9):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h:
            if visited[ny][nx] == 0 and matrix[ny][nx] == 1:
                dfs(nx,ny)
while True:
        w,h = map(int,input().split())
        
        if w==0 and h==0:
            break
            
        matrix = [[0]*w for _ in range(h)]
        visited = [[0]*w for _ in range(h)]

        for i in range(h):
            line = list(map(int,input().split()))
            for j, b in enumerate(line):
                matrix[i][j] = b
        numlist = [] 
        nums=0 
        for a in range(h):
            for b in range(w):
                if matrix[a][b] == 1 and visited[a][b] == 0:
                    dfs(b,a)
                    numlist.append(nums)
                    nums = 0

        print(len(numlist))
