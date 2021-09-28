S=list(input())
li=[-1 for i in range(26)]
for i,s in enumerate(S):
    position = ord(s)-97
    if li[position] == -1:
        li[position]=i
for i in range(26):
    print(li[i],end=' ')
