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
    if not A or i >= len(A):
        return []
    
    pivot = A[i]
    before = []
    equal = []
    after = []
    for j in range(len(A)):
        if (A[j] < pivot):
            before.append(A[j])
        elif (A[j] == pivot):
            equal.append(A[j])
        else:
            after.append(A[j])


    return before + equal + after

print(dutchFlagBruteForce([0,1,2,0,2,1,1], 1))

def dutchFlagTwoPass(A: List[int], i: int) -> List[int]:
    # This solution trades space for time so it takes O(1) space but O(n²) time complexity
    if not A or i>= len(A):
        return []

    pivot = A[i]
    
    # The First pass groups elements smaller than the pivot
    for j in range(len(A)):
        for k in range(j+1, len(A)):
            if(A[k] < pivot):
                A[j], A[k] = A[k], A[j]
                break
        
    # The Second pass groups elements greater than the pivot
    for j in reversed(range(len(A))):
        for k in reversed(range(j)):
            if (A[k] > pivot):
                A[j], A[k] = A[k], A[j]
                break

    return A


print(dutchFlagTwoPass([0,1,2,0,2,1,1], 1))

# There's a better way to do it, with O(n) time complexity and O(1) space complexity
# The problem with the dutchFlagTwoPass solution is, for every element it checks if there are smaller ahead
# but we don't need to start from the beginning, we can do this only when the element being checked is less than the pivot
# so in dutchFlagTwoPass using the array (0,1,2,0,1,1) and the pivot index 1
# in the first pass we actually start at 0 and check each index trying to find an element that is smaller than 0, but we shouldn't
# 0 is already smaller than the pivot so we should just go to the next index

# This is an implementation that is O(n) but uses O(1) space


def dutchFlagSmart(A: List[int], i: int) -> List[int]:
    if(not A or i>= len(A)):
        return []

    pivot = A[i]
    small_index = 0
    big_index = len(A)-1

    for j in range(len(A)):
        if(A[j] < pivot):
            A[j], A[small_index] = A[small_index], A[j]
            small_index += 1
    
    for j in reversed(range(len(A))):
        if(A[j]> pivot):
            A[j], A[big_index] = A[big_index], A[j]
            big_index -=1

    return A

print(dutchFlagSmart([0,1,2,0,2,1,1], 1))