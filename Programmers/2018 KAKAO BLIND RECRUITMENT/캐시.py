def solution(cacheSize, cities):
    answer=0
    cache={}
    cities=[city.lower() for city in cities]
    for city in cities:
        for key,value in cache.items():
            cache[key]+=1
        if city in cache:
            answer+=1
            cache[city]=0
        else:
            answer+=5
            cache[city]=0
            if len(cache)>cacheSize:
                max_city=city
                for key,value in cache.items():
                    if value>cache[max_city]:
                        max_city=key
                del cache[max_city]

    return answer
