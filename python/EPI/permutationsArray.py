# given an array, return the number of possible permutations
from typing import List
def NPermutations(A:List[int]) -> int:
    d = {}
    for i in A:
        d[i] = 0
    result = 1
    for i in reversed(range(1, len(d)+1)):
        result *= i
    return result

print(NPermutations([1,2,3,4,4,5]))
