import sys
read=sys.stdin.readline

n,m=map(int,input().split())
a=list(map(int,read().split()))
b=list(map(int,read().split()))

c=a+b
c.sort()
for i in c:
    print(i,end=' ')
