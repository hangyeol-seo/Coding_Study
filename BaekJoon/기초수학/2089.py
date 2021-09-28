n=int(input())
result=''
if n==0:
    print(n)
else:
    while n:
        if n%2==0:
            result='0'+result
            n=n//(-2)
        else:
            result='1'+result
            n=(n-1)//(-2)
    print(result)
