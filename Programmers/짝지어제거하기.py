def solution(s):
    if len(s)%2==1:
        return 0
    else:
        result=[]
        for i in s:
            if result and result[-1]==i:
                result.pop()
            else:
                result.append(i)
        print(result)
        if result:
            return 0
        else:
            return 1
