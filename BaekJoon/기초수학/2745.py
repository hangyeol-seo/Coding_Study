n,b=input().split()
dic={}
for i in range(10):
    dic[str(i)]=i
for i in range(ord('A'),ord('Z')+1):
    dic[chr(i)]=i-55

result=0
b=int(b)
n=''.join(reversed(n))
for i,j in enumerate(n):
    result+=dic[j]*(b**i)
print(result)
