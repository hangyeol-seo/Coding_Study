import math
def solution(n,a,b):
    dic={}
    cnt=0
    dic[a],dic[b]=a,b
    
    while True:
        if dic[a]==dic[b]:
            break
        if dic[a]>1:
            dic[a]=math.ceil(dic[a]/2)
        if dic[b]>1:
            dic[b]=math.ceil(dic[b]/2)
        cnt+=1
    
    return cnt
