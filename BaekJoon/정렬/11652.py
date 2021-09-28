import sys
n=int(input())
a={}
for i in range(n):
    x=int(sys.stdin.readline())
    if x in a.keys():
        a[x]+=1
    else:
        a[x] = 1
max_num = list(a.keys())[0]
key_list = list(a.keys())
val_list = list(a.values())
for i in range(len(a)):
    k=a[max_num]
    x = val_list[i]
    y = key_list[i]
    if x>k:
        max_num = y
    elif x==k and y<max_num:
        max_num = y
print(max_num)
