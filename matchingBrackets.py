a=str(input())

opening= "[{("
closing = "]})"

def isCorrectMatching(str:str)-> bool:
    l = []
    for i in str:
        if i in opening:
            l.append(i)
        if i in closing:
            if not len(l):
                return False
            c = l.pop()
            if closing.index(i) != opening.index(c):
                return False
    if len(l) == 0:
        return True
    else:
        return False

print(isCorrectMatching(a))