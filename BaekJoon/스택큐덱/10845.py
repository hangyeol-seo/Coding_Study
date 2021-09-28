import sys
n=int(input())
queue=[]
def push(q,x):
    q.append(x)
def pop(q):
    if not q:
        print(-1)
    else:
        print(q[0])
        del q[0]
def size(q):
    print(len(q))
def empty(q):
    if not q:
        print(1)
    else:
        print(0)
def front(q):
    if not q:
        print(-1)
    else:
        print(q[0])
def back(q):
    if not q:
        print(-1)
    else:
        print(q[-1])

for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0]=='push':
        locals()[cmd[0]](queue,cmd[1])
    else:
        locals()[cmd[0]](queue)
