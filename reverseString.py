import time

s = str(input())

def slowReverse(s:str) -> str:
    start_time = time.time()
    l = []
    for i in enumerate(s):
        l.append(s[len(s)-i[0]-1])
    print("%s seconds " %(time.time()-start_time))
    return l

print(slowReverse(s))


def fastReverse(s:str) -> str:
    start_time = time.time()
    reverse = s[::-1]
    print("%s seconds " %(time.time()-start_time))    
    return reverse

print(fastReverse(s))