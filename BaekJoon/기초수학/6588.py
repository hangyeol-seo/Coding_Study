li=[i for i in range(3,1000001-3)]
sosu=[]

for a in li:
    b=int(a**(1/2))
    p=0
    for i in range(2,b+1):
        if a%i==0:
            p=1
            break
    if p==0:
        sosu.append(a)

while True:
    n=int(input())
    x=0
    if n==0:
        break
    for i in sosu:
        if i>n:
            break
        if n-i in sosu:
            print(f'{n} = {i} + {n-i}')
            x=1
            break
    if x==0:
        print("Goldbach's conjecture is wrong.")
