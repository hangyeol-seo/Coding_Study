import sys
read=sys.stdin.readline
def cut(x):
    sum=0
    for i in tree:
        if i-x>=0:
            sum+=(i-x)
    return sum
n,m=map(int,input().split())
tree=list(map(int,read().split()))

l=0
r=max(tree)

while l<=r:
    h=(r+l)//2
    if cut(h)>=m:
        l=h+1
    else:
        r=h-1
print(r)
