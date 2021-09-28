n=int(input())
k=0
picture=[[0 for col in range(n)] for row in range(n)]

def star(x,y,n):
    if n==3:
        picture[x][y:y+3]=[1,1,1]
        picture[x+1][y:y+3]=[1,0,1]
        picture[x+2][y:y+3]=[1,1,1]
        return
    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                continue
            star(x+i*(n//3),y+j*(n//3),n//3)
star(0,0,n)
for i in picture:
    for j in i:
        if j==1:
            print("*",end='')
        else:
            print(" ",end='')
    print()
