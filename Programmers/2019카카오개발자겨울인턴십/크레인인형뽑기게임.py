def solution(board, moves):
    answer = 0
    basket=[]
    for x in moves:
        for y in range(len(board)):
            target=board[y][x-1]
            if target!=0:
                board[y][x-1]=0
                break
        if target!=0:
            if basket and target==basket[-1]:
                basket.pop()
                answer+=2
            else:
                basket.append(target)
    return answer
