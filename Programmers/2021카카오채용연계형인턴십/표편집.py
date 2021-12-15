def solution(n, k, cmd):
    answer=['X']*n
    table=[]
    trash=[]
    for i in range(n):
        table.append(i)
    
    now=k
    for c in cmd:
        if c[0]=='U':
            now-=int(c[2:])
        elif c[0]=='D':
            now+=int(c[2:])
        elif c[0]=='C':
            trash.append((table[now],now))
            del table[now]
            if now==len(table):
                now-=1
        else:
            value,idx=trash.pop()
            table.insert(idx,value)
            if idx<=now:
                now+=1
                
    for val in table:
        answer[val]='O'
    
    return ''.join(answer)
