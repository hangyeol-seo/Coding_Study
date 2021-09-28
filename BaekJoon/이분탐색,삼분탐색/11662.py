Ax,Ay,Bx,By,Cx,Cy,Dx,Dy=map(int,input().split())

speedx_AtoB = Bx-Ax
speedy_AtoB = By-Ay
speedx_CtoD = Dx-Cx
speedy_CtoD = Dy-Cy

def dis_cal(Ax,Ay,Bx,By):
    return (((Bx-Ax)**2)+((By-Ay)**2))**(1/2)

def pos_cal(t):
    Pxt=Ax+speedx_AtoB*t
    Pyt=Ay+speedy_AtoB*t
    Qxt=Cx+speedx_CtoD*t
    Qyt=Cy+speedy_CtoD*t
    return dis_cal(Pxt,Pyt,Qxt,Qyt)

lo,hi = 0,1
minimum=min(pos_cal(lo),pos_cal(hi))

while hi-lo>=10**(-6):
    p,q=(2*lo+hi)/3,(lo+2*hi)/3
    p_val = pos_cal(p)
    q_val = pos_cal(q)
    if p_val>=q_val:
        lo=p
        minimum=min(minimum,q_val)
    else:
        hi=q
        minimum=min(minimum,p_val) 
print(minimum)
