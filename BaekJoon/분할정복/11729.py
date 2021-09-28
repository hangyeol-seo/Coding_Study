cnt=0
result=[]

def hanoi(n,start,through,end):
    global cnt
    if(n==1):
        cnt+=1
        result.append((start,end))
        return
    else:
        hanoi(n-1,start,end,through)
        cnt+=1
        result.append((start,end))
        hanoi(n-1,through,start,end)
        
n=int(input())
hanoi(n,1,2,3)
print(cnt)
for i in result:
    print(i[0],i[1])
