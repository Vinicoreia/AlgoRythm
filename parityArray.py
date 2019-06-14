
class Solution:
    def sortArrayByParity(self, A):
        even = [i if i%2==0 for i in A]
        odd = [o if o%2==1 for o in A]

        return even+odd