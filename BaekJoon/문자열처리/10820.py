while True:
    try:
        result=[0,0,0,0]
        S=list(input())
        for s in S:
            if 97<=ord(s)<=122:
                result[0]+=1
            elif 65<=ord(s)<=90:
                result[1]+=1
            elif 48<=ord(s)<=57:
                result[2]+=1
            elif ord(s)==32:
                result[3]+=1
        for i in result:
            print(i,end=' ')
    except EOFError:
        break
