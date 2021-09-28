N,K = map(int,input().split())
people=[i+1 for i in range(N)]
position=-1
s="<"
for c in range(N):
    i=0
    for i in range(K):
        position+=1
        if position>=len(people):
            position=0
            people=[val for val in people if val!=0]
    s=s+str(people[position])+', '
    people[position]=0
print(s[:-2]+">")
