def div(n):
    m=int(n**(1/2))
    d=n
    for i in range(2,m+1):
        if n%i==0:
            d=i
            break
    return d
    
n=int(input())
if n!=1:
    while True:
        divisor=div(n)
        print(divisor)
        if divisor==n:
            break
        else:
            n=n//divisor
