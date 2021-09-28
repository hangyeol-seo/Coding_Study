a=list(input())
li=[]
result=0
r=0
for i in a:
    if i=='(':
        li.append(i)
        r=0
    else:
        if r==0:
            li.pop()
            result+=len(li)
            r=1
        else:
            result+=1
            li.pop()
print(result)
