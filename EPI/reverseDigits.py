# Write a program that takes an integer and returns another integer which has the digits reversed
# input: 34
# output: 43
# input: -152
# output: -251

def bruteForceReverse(x:int) -> int:
    s = str(x)
    if(s[0] =='-'):
        rev = s[1::]
        return  - int(rev[::-1])
    else:
        rev = s[::-1]
        return int(rev)


def smartReverseInt(x:int) -> int:
    remainder = abs(x)
    result = 0

    while(remainder):
        result *=10 
        result += remainder%10
        remainder //= 10
    return result if x>0 else -result

print(smartReverseInt(10))
print(smartReverseInt(501))
print(smartReverseInt(105))
print(smartReverseInt(-132441))
