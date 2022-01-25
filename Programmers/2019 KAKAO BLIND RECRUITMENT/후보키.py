from itertools import combinations
import numpy as np
def solution(relation):
    answer = 0
    length=len(relation[0])
    height=len(relation)
    for i in range(length):
        chk=0
        for j in range(length-i):
            tmp1=tuple([i])
            tmp2=tuple(combinations(np.arange(i+1,length),j))
            for x in tmp2:
                comb=tmp1+tuple(x)
                print(comb)
                tmp_set=set()
                for k in range(height):
                    target=tuple(relation[k][y] for y in comb)
                    tmp_set.add(target)
                if len(tmp_set)==height:
                    answer+=1
                    chk=1
                    break
            if chk==1:
                break
            
    return answer
