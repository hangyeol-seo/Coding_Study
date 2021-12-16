def shift(s,node,table):
    if s==0:
        return s,node
    if s>0:
        for _ in range(s):
            node=table[node][1]
    else:
        for _ in range(-s):
            node=table[node][0]
    s=0
    return s,node

def solution(n, k, cmd):
    answer=['O' for _ in range(n)]
    table={}
    trash=[]
    for i in range(n):
        table[i]=[i-1,i+1]
    table[0][0]=None
    table[n-1][1]=None
    
    s=0
    node=k
    for c in cmd:
        if c[0]=='U':
            s-=int(c[2:])
        elif c[0]=='D':
            s+=int(c[2:])
        elif c[0]=='C':
            s,node=shift(s,node,table)
            trash.append(node)
            if table[node][0]!=None:
                table[table[node][0]][1]=table[node][1]
            if table[node][1]!=None:
                table[table[node][1]][0]=table[node][0]
                node=table[node][1]
            else:
                node=table[node][0]
        else:
            s,node=shift(s,node,table)
            x=trash.pop()
            if table[x][0]!=None:
                table[table[x][0]][1]=x
            if table[x][1]!=None:
                table[table[x][1]][0]=x
    
    for node in trash:
        answer[node]='X'
    
    return ''.join(answer)
