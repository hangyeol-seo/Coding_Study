from itertools import permutations

def solution(expression):
    operator=[]
    operand=[]
    num=''
    answer=0
    for i,e in enumerate(expression):
        if e in '+-*':
            operator.append(e)
            operand.append(int(num))
            num=''
        else:
            num+=e
        if i==len(expression)-1:
            operand.append(int(num))    

    for perm in permutations(set(operator),len(set(operator))):
        operand_cpy=operand.copy()
        operator_cpy=operator.copy()
        for op in perm:
            while op in operator_cpy:
                index=operator_cpy.index(op)
                result=eval(str(operand_cpy[index])+op+str(operand_cpy[index+1]))
                operand_cpy[index]=result
                del operand_cpy[index+1]
                del operator_cpy[index]
        answer=max(answer,abs(operand_cpy[0]))
    return answer
