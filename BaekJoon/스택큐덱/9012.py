import sys
n=int(input())
for i in range(n):
    ps_list=list(sys.stdin.readline())
    li=[]
    result=0
    for j in ps_list:
        if j=='(':
            li.append(j)
        elif j==')':
            if not li:
                sys.stdout.write('NO\n')
                result=1
                break
            else:
                li.pop()
    if result==1:
        continue
    if not li:
        sys.stdout.write('YES\n')
    else:
        sys.stdout.write('NO\n')
