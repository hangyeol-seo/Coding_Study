import sys
read=sys.stdin.readline

def count(x):
    cnt=0
    for i in lan_list:
        cnt+=(i//x)
    return cnt

k,n=map(int,input().split())
lan_list=[]
for i in range(k):
    lan_list.append(int(read()))

l=1
r=max(lan_list)

while l<=r:
    m=(r+l)//2
    c=count(m)
    if c>=n:
        l=m+1
    else:
        r=m-1
print(r)
