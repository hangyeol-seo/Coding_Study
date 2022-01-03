def num_to_arr(n,num):
    result=''
    num=bin(num)[2:].rjust(n,'0')
    for i in num:
        if i=='0':
            result+=' '
        else:
            result+='#'
    return result

def solution(n, arr1, arr2):
    answer=[i|j for i,j in zip(arr1,arr2)]
    return [num_to_arr(n,i) for i in answer]
