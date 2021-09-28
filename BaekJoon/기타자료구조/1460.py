import sys
s=sys.stdin.readline().strip()
s1=list(s)
s2=[]
n=int(input())

for i in range(n):
    x = sys.stdin.readline().strip()
    cmd = x[0]
    if cmd=='L':
        if s1:
            s2.append(s1.pop())
    elif cmd=='D':
        if s2:
            s1.append(s2.pop())
    elif cmd=='B':
        if s1:
            s1.pop()
    elif cmd=='P':
        s1.append(x[2])
s2.reverse()
print(''.join(s1+s2))
