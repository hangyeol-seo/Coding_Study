import sys
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
T=int(input())
for t in range(T):
    li=input().split()
    n=int(li[0])
    a=list(map(int,li[1:]))
    result=0
    for i in range(n):
        for j in range(i+1,n):
            result+=gcd(a[i],a[j])
    print(result)
