from typing import List
class Solution:
    def sortArrayByParity(self, A):
        even = [i for i in A if i%2==0]
        odd = [o for o in A if o%2==1]

        return even+odd


# New Solution using O(1) space
    def even_odd(self, A: List[int]):
        even, odd = 0, len(A)-1
        while(even < odd):
            if(A[even]%2 ==0):
                even+=1
            else:
                A[even], A[odd] = A[odd], A[even]
                odd-=1
        return A

