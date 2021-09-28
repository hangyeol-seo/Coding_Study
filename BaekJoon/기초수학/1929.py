m,n=map(int,input().split())
li=[i for i in range(m,n+1)]
result=[]
while 1 in li:
    li.remove(1)
for a in li:
    b=int(a**(1/2))
    p=0
    for i in range(2,b+1):
        if a%i==0:
            p=1
            break
    if p==0:
        result.append(a)
for i in result:
    print(i)
