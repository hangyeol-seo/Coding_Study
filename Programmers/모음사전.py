from itertools import product
def solution(word):
    words=['','A','E','I','O','U']
    l=[]
    for w in product(words,repeat=5):
        data=''.join(w)
        if data not in l:
            l.append(data)
    l.sort()
    return l.index(word)
