import sys
a=[]
n=int(input())
for i in range(n):
    age,name = sys.stdin.readline().split()
    a.append((int(age),i,name))
a.sort()
for i in range(n):
    print(a[i][0],a[i][2])
