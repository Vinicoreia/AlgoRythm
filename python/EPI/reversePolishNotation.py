def RPN(s):
    result  = []
    operations = {
        '+': lambda x,y: x + y,
        '*': lambda x,y: x * y,
        '/': lambda x,y: y / x,
        '-': lambda x,y: y - x,
    }


    for token in s.split(' '):
        if(token in operations):
            result.append(operations[token](result.pop(), result.pop()))
        else:
            result.append(int(token))
    return result

print(RPN('3 4 +'))

