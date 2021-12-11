def calculate_time(start,end):
    start_h,start_m=start.split(':')
    end_h,end_m=end.split(':')
    return (int(end_h)*60+int(end_m))-(int(start_h)*60+int(start_m))

def note_to_num(note):
    num_dic={}
    result=[]
    num_dic['C']=0;num_dic['D']=2;num_dic['E']=4;num_dic['F']=5;num_dic['G']=7
    num_dic['A']=9;num_dic['B']='b'
    for i in note:
        if i=='#':
            if result[-1]==9:
                result[-1]='a'
            else:
                result[-1]+=1
        else:
            result.append(num_dic[i])
    return ''.join(map(str,result))

def solution(m, musicinfos):
    possible=[]
    info_dic={}
    m=note_to_num(m)

    for info in musicinfos:
        start,end,title,note = info.split(',')
        length=calculate_time(start,end)
        note=note_to_num(note)
        notes=note*(length//len(note))
        notes+=note[:(length%len(note))]
        if m in notes:
            possible.append(title)
            info_dic[title]=length
                  
    if possible:
        answer=possible[0]
        for i in possible[1:]:
            if info_dic[i]>info_dic[answer]:
                answer=i
    else:
        answer='(None)'
    return answer
