import sys
read=sys.stdin.readline
input()
n=list(map(int,read().split()))
input()
m=list(map(int,read().split()))
dic={}
for i in n:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

for i in m:
    if i in dic:
        print(dic[i],end=' ')
    else:
        print(0,end=' ')
