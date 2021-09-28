import sys
read=sys.stdin.readline
input()
n = set(map(int, read().split()))
input()
m = list(map(int, read().split()))
for i in m:
    if i in n:
        print(1, end=' ')
    else:
        print(0, end=' ')
