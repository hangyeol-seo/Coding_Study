def solution(stones, k):
    start,end=0,2*(10**8)+1
    
    while start<end:
        mid=(start+end)//2
        cnt=0
        for stone in stones:
            if stone<=mid:
                cnt+=1
            else:
                cnt=0
            if cnt==k:
                break
        if cnt==k:
            end=mid
        else:
            start=mid+1

    return end
