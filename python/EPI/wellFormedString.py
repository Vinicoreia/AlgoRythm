


def wellFormedString(s):
    stack = []
    d = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    for letter in s:
        if(letter in d):
            stack.append(letter)
        elif not stack or letter != d[stack.pop()]:
            return False
    return not stack

print(wellFormedString('(())'))
print(wellFormedString('(()'))
print(wellFormedString("({})[]"))