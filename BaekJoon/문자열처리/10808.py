S=list(input())
li=[0 for i in range(26)]
for s in S:
    li[ord(s)-97]+=1
for i in range(26):
    print(li[i],end=' ')
