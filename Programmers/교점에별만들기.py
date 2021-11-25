from itertools import combinations as comb
def solution(line):
    x_cord = []
    y_cord=[]
    answer=[]

    for l1,l2 in comb(line,2):
        A,B,C,D,E,F=l1[0],l1[1],l2[0],l2[1],l1[2],l2[2]
        if A*D-B*C!=0:
            x=(B*F-E*D)/(A*D-B*C)
            y=(E*C-A*F)/(A*D-B*C)
            if int(x)==x and int(y)==y:
                x_cord.append(int(x))
                y_cord.append(int(y))

    max_x,min_x=max(x_cord),min(x_cord)
    max_y,min_y=max(y_cord),min(y_cord)

    for i in range(len(x_cord)):
        x_cord[i]-=min_x
        y_cord[i]-=max_y
        y_cord[i]*=-1

    result=[['.' for _ in range(max_x-min_x+1)] for _ in range(max_y-min_y+1)]
    for i,j in zip(x_cord,y_cord):
        result[j][i]='*'
    for i in result:
        answer.append(''.join(i))
    return answer
