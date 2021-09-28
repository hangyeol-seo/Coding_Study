S=list(input())
for s in S:
    if 65<=ord(s)<=77:
        print(chr(ord(s)+13),end='')
    elif 78<=ord(s)<=90:
        print(chr(ord(s)-13),end='')
    elif 97<=ord(s)<=109:
        print(chr(ord(s)+13),end='')
    elif 110<=ord(s)<=122:
        print(chr(ord(s)-13),end='')
    else:
        print(s,end='')
