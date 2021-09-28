import sys

def move_Case1(r,c):
    result=''
    for i in range(c//2):
        result+="D"*(r-1)
        result+="R"
        result+="U"*(r-1)
        result+="R"
    result+="D"*(r-1)
    print(result)

def move_Case2(r,c):
    result=''
    for i in range(r//2):
        result+="R"*(c-1)
        result+="D"
        result+="L"*(c-1)
        result+="D"
    result+="R"*(c-1)
    print(result)

def move_Case3(mat,r,c):
    minimum = 1000
    for i in range(r):
        for j in range(c):
            if((i+j)%2!=0 and minimum>mat[i][j]):
                minimum=mat[i][j]
                position=(i,j)
    result = ('D'*(r-1)+'R'+'U'*(r-1)+'R')*(position[1]//2)
    X=2*(position[1]//2)
    Y=0
    X_MAX=2*(position[1]//2)+1
    while X!=X_MAX or Y!=r-1:
        if(X<X_MAX and (Y,X_MAX)!=position):
            X+=1
            result+='R'
        elif X == X_MAX and (Y, X_MAX - 1) != position:
            X -= 1
            result += 'L'
        if Y != r - 1:
            Y += 1
            result += 'D'
    result += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - position[1] - 1) // 2)
    print(result)

R,C = map(int,input().split())
matrix=[[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    matrix[i] = list(map(int,input().split()))
    
if(C%2!=0):
    move_Case1(R,C)
elif(R%2!=0):
    move_Case2(R,C)
else:
    move_Case3(matrix,R,C)
