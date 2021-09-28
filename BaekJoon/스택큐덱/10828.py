import sys
n=int(input())
a=[]

def push(x,y):
    x.append(y)
    
def pop(x):
    if not x:
        print(-1)
    else:
        k=x.pop()
        print(k)
        
def size(x):
    print(len(x))
    
def empty(x):
    if not x:
        print(1)
    else:
        print(0)
        
def top(x):
    if not x:
        print(-1)
    else:
        print(x[-1])
        
for i in range(n):
    cmd=sys.stdin.readline().split()
    if len(cmd)>1:
        locals()[cmd[0]](a,cmd[1])
    else:
        locals()[cmd[0]](a)
