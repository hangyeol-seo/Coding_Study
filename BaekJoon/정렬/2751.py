import sys

n=int(input())
num_list=[int(sys.stdin.readline()) for i in range(n)]
num_list.sort()
for i in range(n):
    print(num_list[i])
