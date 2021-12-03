def solution(numbers, hand):
    answer = ''
    pos_dic={1:(0,3),2:(1,3),3:(2,3),4:(0,2),5:(1,2),6:(2,2),7:(0,1),8:(1,1),9:(2,1),0:(1,0)}
    now_left,now_right=(0,0),(2,0)
    for number in numbers:
        if number in [1,4,7]:
            now_left=pos_dic[number]
            answer+='L'
        elif number in [3,6,9]:
            now_right=pos_dic[number]
            answer+='R'
        else:
            left_dist,right_dist=0,0
            for a,b,c in zip(pos_dic[number],now_left,now_right):
                left_dist+=abs(b-a)
                right_dist+=abs(c-a)
            if left_dist<right_dist:
                now_left=pos_dic[number]
                answer+='L'
            elif left_dist>right_dist:
                now_right=pos_dic[number]
                answer+='R'
            else:
                if hand=='left':
                    now_left=pos_dic[number]
                    answer+='L'
                else:
                    now_right=pos_dic[number]
                    answer+='R'
    return answer
