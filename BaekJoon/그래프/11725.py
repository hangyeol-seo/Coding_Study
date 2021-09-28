import sys
read=sys.stdin.readline
sys.setrecursionlimit(10**8)
n=int(input())
tree={}
parent={}

for i in range(1,n+1):
    parent[i]=0
    tree[i]=0
    
def find_parent(node):
    for i in tree[node]:
        if parent[i]==0:
            parent[i]=node
            find_parent(i)
                
for _ in range(n-1):
    data1,data2 = map(int,read().split())
    if tree[data1]==0:
        tree[data1]=[data2]
    else:
        tree[data1].append(data2)
    if tree[data2]==0:
        tree[data2]=[data1]
    else:
        tree[data2].append(data1)
        
find_parent(1)
for i in range(2,n+1):
    print(parent[i])
