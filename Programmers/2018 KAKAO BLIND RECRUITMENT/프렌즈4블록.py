def check_block(m,n,board):
    x=[0,1,1]
    print(x)
    y=[1,0,1]
    result=set()
    for i in range(m-1):
        for j in range(n-1):
            target=board[i][j]
            if target=='':
                continue
            tmp=[(i,j)]
            for dx,dy in zip(x,y):
                ny,nx=i+dy,j+dx
                if board[ny][nx]=='':
                    break
                if board[ny][nx]==target:
                    tmp.append((i+dy,j+dx))
            if len(tmp)==4:
                for element in tmp:
                    result.add(element)
    return result

def clear_block(m,n,board,result):
    for i,j in result:
        board[i][j]=0
    for i in range(1,m):
        for j in range(n):
            if board[i][j]==0:
                for k in range(i,-1,-1):
                    board[k][j]=board[k-1][j]
                board[0][j]=''
    return board
def solution(m, n, board):
    answer = 0
    board=[list(board[i]) for i in range(m)]
    while True:
        result=check_block(m,n,board)
        if len(result)==0:
            break
        answer+=len(result)
        board=clear_block(m,n,board,result)
    return answer


  
