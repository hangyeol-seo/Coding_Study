def solution(sizes):
    w=[]
    h=[]
    for i,j in sizes:
        e_w,e_h=max(i,j),min(i,j)
        w.append(e_w)
        h.append(e_h)


    return max(w)*max(h)
