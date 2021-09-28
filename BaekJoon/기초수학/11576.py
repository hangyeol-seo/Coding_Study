a,b=map(int,input().split())
m=int(input())
li=list(map(int,input().split()))
n=0
result=[]
li.reverse()
for i in range(len(li)):
    n+=li[i]*(a**i)
if n==0:
    print(n)
else:
    while n:
        result.append(n%b)
        n=n//b
result.reverse()
for i in result:
    print(i,end=' ')
