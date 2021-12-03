import sys
sys.setrecursionlimit(10**8)

def find_room(number, room):
    if number not in room:
        room[number] = number + 1
        return number

    empty = find_room(room[number], room)
    room[number] = empty + 1
    return empty

def solution(k, room_number):
    answer = []

    dic = {}

    for i in room_number:
        num = find_room(i, dic)
        answer.append(num)

    return answer
