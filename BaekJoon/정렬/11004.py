import sys

n,k=map(int,sys.stdin.readline().split())
num_list = list(map(int,input().split()))
num_list.sort()
print(num_list[k-1])
