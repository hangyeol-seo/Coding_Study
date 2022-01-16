def solution(cacheSize, cities):
    answer=0
    cache={}
    for c in cities:
        city=c.lower()
        for key,value in cache.items():
            cache[key]+=1
        if city in cache:
            answer+=1
            cache[city]=0
        else:
            answer+=5
            cache[city]=0
            if len(cache)>cacheSize:
                target=city
                for key,value in cache.items():
                    if value>cache[target]:
                        target=key
                del cache[target]

    return answer
