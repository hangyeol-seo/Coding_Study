from itertools import product

def solution(user_id, banned_id):
    answer=[]
    result=[]
    visited=[]
    for b_id in banned_id:
        possible=[]
        for u_id in user_id:
            chk=0
            if len(b_id)!=len(u_id):
                continue
            for b,u in zip(b_id,u_id):
                if b!='*' and b!=u:
                    chk=0
                    break
                chk+=1
            if chk==len(b_id):
                possible.append(u_id)
        result.append(possible)
    for i in product(*result):
        data=set(i)
        if len(data)==len(banned_id) and data not in answer:
            answer.append(data)   
    return len(answer)
