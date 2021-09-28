n=int(input())
cnt5=0
cnt2=0
for i in range(1,n+1):
    while True:
        if i%5==0:
            i=i//5
            cnt5+=1
        elif i%2==0:
            i=i//2
            cnt2+=1
        else:
            break
print(min(cnt5,cnt2))
