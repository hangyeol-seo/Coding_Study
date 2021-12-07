from collections import defaultdict,deque

def bfs(start,cave_map,orders):
    visited=set([])
    queue=deque([start])
    after={}
    while queue:
        n=queue.popleft()
        if n in orders and orders[n] not in visited:
            after[orders[n]]=n
            continue 
        visited.add(n)
        for i in cave_map[n]:
            if i not in visited:   
                queue.append(i)
        if n in after:
            queue.append(after[n])

    return len(visited)

def solution(n, path, order):
    cave_map=defaultdict(list)
    orders={}
    for n1,n2 in path:
        cave_map[n1].append(n2)
        cave_map[n2].append(n1)
    for n1,n2 in order:
        orders[n2]=n1 
    result=bfs(0,cave_map,orders)
    if result==n:
        return True
    return False
