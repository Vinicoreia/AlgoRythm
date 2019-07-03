from typing import List
def removeDuplicates(A:List[int]) -> List[int]:
    if(not A):
        return []
    
    i = 1
    for j in range(1, len(A)):
        if(A[i -1] != A[j]):
            A[i] = A[j]
            i+=1
    return A[:i]

print(removeDuplicates([1,1,2,3,4,5,5,6,7,7,7,8,8,9]))