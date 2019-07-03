from typing import List
import math


# The Buy and Sell is a common problem and this is a brute force way to do it
# This is really bad and takes O(n²) time 
# for maximization and minimization problem we usually can use Divide and conquer or greedy algorithms.

def buySellOnceBad(A: List[int]) -> int:
    maxi = -1

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if(A[j]-A[i]> maxi):
                maxi = A[j]-A[i]

    return maxi

print(buySellOnceBad([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))


# If we think about it, we can do it in O(n) time by recording the minimum element seen so far for each element we see
# The maximum profit of the day would be the value we are visiting minus the minimum element we saw until getting there

def buySellOnce_N(A:List[int]) -> int:
    minimum = math.inf
    maxi = -1
    for i in range(len(A)):
        minimum = min(minimum, A[i])
        maxi = max(A[i]-minimum, maxi)
    return maxi
print(buySellOnce_N([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
