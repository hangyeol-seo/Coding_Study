numsystem='0123456789'
SDTsystem='SDT'

def solution(dartResult):
    number=[]
    SDT=[]
    op=[]
    num=''
    for i in dartResult:
        if i in numsystem:
            num+=i
        elif i in SDTsystem:
            number.append(num)
            num=''
            SDT.append(i)
            op.append('')
        else:
            op[-1]+=i
    calculate=[]
    for i,j,k in zip(number,SDT,op):
        array='('+i
        if j=='S':
            array+='**1)'
        elif j=='D':
            array+='**2)'
        elif j=='T':
            array+='**3)'
        if k=='*':
            if calculate!=[]:
                calculate[-1]+='*2'
            array+='*2'
        elif k=='#':
            array+='*(-1)'
        calculate.append(array)
        answer=0
        for i in calculate:
            answer+=eval(i)
    return answer
