# Suppose you have an array like [3,3,1,0,2,0,1]
# every number in the array is the number of steps you can give towards the end of the array
# Write a program that returns True if the end can be reached and false if you can not reach the end

# In the array of the example [3,3,1,0,2,0,1] you can reach the end by
# move 1 to index 1, move 3 to index 4, move 2 to index 6 and move 1 to the end
# you can take 3 steps but you don't necessarily have to do so.


from typing import List
def advanceOffset(A:List[int]) -> bool:
    # How far can we get from index i?
    # i + A[i]
    reach = 0
    i = 0

    while( i<= reach and reach < len(A)): 
        reach = max(reach, i + A[i]) # maximum reach is where i can go from that point
        i += 1
    return reach >= len(A)

print(advanceOffset([3,3,4,0,2,0,0]))
