from typing import List

#  This is O(n) time complexity and O(1) space
# We keep a pointer that increases everytime the elements are different
# If they are equal only the iterator j increments
# then when they are different again we change the last element that was a duplicate with a different element present in the array
# Since we only have to pass the whole array once the time complexity is O(n)
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

# in python we can just return a set as well

def oneLinerRemoveDuplicates(A:List[int]) -> List[int]:
    return list(set(A))

print(oneLinerRemoveDuplicates([1,1,2,3,4,5,5,6,7,7,7,8,8,9]))
