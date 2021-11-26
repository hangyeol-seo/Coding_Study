from collections import defaultdict
import copy

def dfs(n,tmp_dic):
    result=set()
    for i in range(1,n+1):
        visited=[i]
        stack=[i]
        cnt=1
        while stack:
            x=stack.pop()
            for j in tmp_dic[x]:
                if j not in visited:
                    cnt+=1
                    stack.append(j)
                    visited.append(j)
        result.add(cnt)
    return result

def solution(n, wires):
    dic=defaultdict(list)
    answer=[]
    for x,y in wires:
        dic[x].append(y)
        dic[y].append(x)
    for l1,l2 in wires:
        tmp_dic=copy.deepcopy(dic)
        tmp_dic[l1].remove(l2)
        tmp_dic[l2].remove(l1)
        tmp_result=dfs(n,tmp_dic)
        answer.append(max(tmp_result)-min(tmp_result))
    return min(answer)
