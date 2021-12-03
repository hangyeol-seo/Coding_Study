def solution(gems):
    answer=[0,len(gems)-1]
    start,end=0,0
    container={gems[0]:1}
    length=len(set(gems))
    
    while start<=end:
        if len(container)==length:
            if end-start < answer[1]-answer[0]:
                answer=[start,end]
            container[gems[start]]-=1
            if container[gems[start]]==0:
                del(container[gems[start]])
            start+=1
            
        else:
            end+=1
            if end==len(gems):
                break
            if gems[end] not in container:
                container[gems[end]]=1
                
            else:
                container[gems[end]]+=1
                
    return [answer[0]+1,answer[1]+1]
