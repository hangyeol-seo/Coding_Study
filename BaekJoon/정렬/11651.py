import sys

a=[]
n=int(input())
for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    a.append((y,x))
a.sort()
for i in range(n):
    print(a[i][1],a[i][0])
