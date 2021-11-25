from itertools import permutations
def solution(k, dungeons):
    cnts=[]
    P=permutations(dungeons,len(dungeons))
    for a in P:
        cnt=0
        tired=k
        for b,c in a:
            if b<=tired:
                tired-=c
                cnt+=1
            else:
                break
        cnts.append(cnt)
    return max(cnts)
