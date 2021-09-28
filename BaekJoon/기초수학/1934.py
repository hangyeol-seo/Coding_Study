def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    g=gcd(a,b)
    print((a*b)//g)
