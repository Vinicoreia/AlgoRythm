# The Dutch Flag Partition is used to kind of teach how a quick sort works
# You're a given a array of 0's, 1's and 2's and a pivot
# Then you must build a function to rearrange this array such that:
# All numbers smaller than the pivot must be to it's left
# All numbers bigger than the pivot must be to it's right

# Suppose the array A = (0,1,2,0,2,1,1) and the pivot index is 3
# this means A[3] is 0 so a valid partitioning would be (0,0,1,2,2,1,1) but (0,0,1,2,1,2,1) is also a valid partition
# if the pivot index is 5 then a valid partition would be (0,0,1,1,1,2,2)


# Write a program that takes an array A and an index i into A and rearranges the elements such that all elements
# less than A[i] appear first, followed by elements equal to A[i], followed by elements greater than A[i].

from typing import List

def dutchFlagBruteForce(A: List[int], i: int) -> List[int]:
    #Using O(n) time and O(n) space
    if not A or i > len(A):
        return []
    
    pivot = A[i]
    before = []
    equal = []
    after = []
    for j in range(len(A)):
        if A[j] < pivot:
            before.append(A[j])
        elif A[j] == pivot:
            equal.append(A[j])
        else:
            after.append(A[j])


    return before + equal + after

print(dutchFlagBruteForce([0,1,2,0,2,1,1], 1))