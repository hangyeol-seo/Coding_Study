def solution(s):
    dic={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    num='0123456789'
    tmp=''
    answer=''
    for i in s:
        if i in num:
            answer+=i
            continue
        tmp+=i
        if tmp in dic:
            answer+=dic[tmp]
            tmp=''
    return int(answer)
