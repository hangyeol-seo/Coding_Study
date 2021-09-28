import sys
read=sys.stdin.readline
N = int(input())

video = [list(map(int,list(input()))) for _ in range(N)]
def compress(x, y, n):
    
    num_check = video[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if(video[i][j] != num_check):
                print('(',end='')
                for k in range(2):
                    
                    for l in range(2):
                        compress(x + k * n//2, y + l * n//2, n//2)
                print(')',end='')
                return
            
    if(num_check == 0):
        print(0,end='')
    else:
        print(1,end='')
        
compress(0, 0, N)
