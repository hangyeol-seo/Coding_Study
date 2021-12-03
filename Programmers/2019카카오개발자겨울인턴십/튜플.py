def solution(s):
    answer = []
    l=[]
    num=''
    for x in s[1:-1]:
        if x=='{':
            l.append(set())
        elif (x==',' and num!='') or x=='}':
            l[-1].add(int(num))
            num=''
        elif x!=',' :
            num+=x
            
    
    l=sorted(l,key=lambda x: len(x))
    answer+=l[0]
    for i in range(1,len(l)):
        answer+=list(l[i]-l[i-1])
    return answer
