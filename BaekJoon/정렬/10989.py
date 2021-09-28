import sys

n=int(input())
a= [0 for i in range(10001)]
for i in range(1,n+1):
    a[int(sys.stdin.readline())]+=1
for i in range(1,10001):
    for j in range(a[i]):
        print(i)
