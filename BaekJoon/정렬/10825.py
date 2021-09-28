import sys
n = int(input())
a=[]

for i in range(n):
    name,korean,english,math = sys.stdin.readline().split()
    a.append([int(korean),int(english),int(math),name])
a=sorted(a,key=lambda x:(-x[0],x[1],-x[2],x[3]))

for i in range(n):
    print(a[i][3])
