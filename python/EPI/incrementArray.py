# You receive an array such as [1,2,9] you must increment it by 1 and return another array
# in this case [1,3,0]

from typing import List

def incrementArray(A: List[int]) -> List[int]:
    if( not A):
        return []
    
    A[-1] += 1 # Increment the last number and see if it would result in a carry
    carry = 0
    for i in reversed(range(len(A))):
        if(carry == 1):
            A[i] += 1
        if(A[i] == 10):
            A[i] = 0
            carry = 1
        else:
            carry = 0
            break
        
    if(carry == 1 or A[0] == 10):
        A[0] = 1
        A.append(0)
    return A

print(incrementArray([9]))
print(incrementArray([9,9]))
print(incrementArray([8,9]))
print(incrementArray([1,2]))
print(incrementArray([9,9,9,9,9]))
