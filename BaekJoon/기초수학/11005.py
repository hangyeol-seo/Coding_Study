n,b=map(int,input().split())
dic={}
for i in range(10):
    dic[i]=str(i)
for i in range(10,36):
    dic[i]=chr(ord('A')+i-10)
s=''
while True:
    r=n%b
    n=n//b
    s+=dic[r]
    if n==0:
        break
print(''.join(reversed(s)))
