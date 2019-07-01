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

print(bruteForceReverse(10))
print(bruteForceReverse(105))
print(bruteForceReverse(-10410))