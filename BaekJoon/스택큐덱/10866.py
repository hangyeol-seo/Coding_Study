import sys

n=int(input())
dequeue=[]

def push_front(dq,x):
    dq.reverse()
    dq.append(x)
    dq.reverse()
def push_back(dq,x):
    dq.append(x)
def pop_front(dq):
    if not dq:
        print(-1)
    else:
        print(dq[0])
        del dq[0]
def pop_back(dq):
    if not dq:
        print(-1)
    else:
        print(dq[-1])
        del dq[-1]
def size(dq):
    print(len(dq))
def empty(dq):
    if not dq:
        print(1)
    else:
        print(0)
def front(dq):
    if not dq:
        print(-1)
    else:
        print(dq[0])
def back(dq):
    if not dq:
        print(-1)
    else:
        print(dq[-1])

for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0]=='push_back' or cmd[0]=='push_front':
        locals()[cmd[0]](dequeue,cmd[1])
    else:
        locals()[cmd[0]](dequeue)
