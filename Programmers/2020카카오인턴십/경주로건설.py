from collections import deque,defaultdict

def is_straight(direc,dir_past,dir_now):
    if dir_past==None:
        return True
    if dir_past==dir_now:
        return True
    return False
  
def calculate(direc,money,past,now,now_direc):
    tmp_money=[]
    for i,d in enumerate(direc[past]):
        if is_straight(direc,d,now_direc):
            tmp_money.append(money[past][i]+100)
        else:
            tmp_money.append(money[past][i]+600)
            
    data=min(tmp_money)
    if direc[now] and now_direc in direc[now]:
        for i,d in enumerate(direc[now]):
            if d==now_direc:
                if money[now][i] >data:
                    money[now][i]=data
                    return True
                else:
                    return False
    else:            
        money[now].append(data)
        direc[now].append(now_direc)
        return True


    
def bfs(start,board,end):
    direc=defaultdict(list)
    direc[start].append(None)
    queue=deque([start])
    money=defaultdict(list)
    money[start].append(0)
    length=len(board)-1
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    while queue:
        n=queue.popleft()
        for nx,ny in zip(dx,dy):
            next=(n[0]+nx,n[1]+ny)
            if 0<=next[0]<=length and 0<=next[1]<=length and board[next[1]][next[0]]==0:
                if next not in money:
                    calculate(direc,money,n,next,(nx,ny))
                    queue.append(next)
                elif calculate(direc,money,n,next,(nx,ny)):
                    queue.append(next)
    return min(money[end])
                    
    
def solution(board):
    return bfs((0,0),board,(len(board)-1,len(board)-1))
