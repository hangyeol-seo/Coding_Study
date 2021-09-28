n=input()
x=set(n)
if '0' not in x:
    print(-1)
else:
    x=list(map(int,list(n)))
    if sum(x)%3!=0:
        print(-1)
    else:
        result=''
        x=sorted(x,reverse=True)
        for i in x:
            result+=str(i)
        print(result)
