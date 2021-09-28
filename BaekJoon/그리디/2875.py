n,m,k=map(int,input().split())
temp_girl=0
temp_boy=0
while temp_girl+temp_boy<k:
    if n>2*m:
        temp_girl+=n-2*m
        n-=(n-2*m)
    else:
        temp_boy+=1
        m-=1
print(min(m,n//2))
