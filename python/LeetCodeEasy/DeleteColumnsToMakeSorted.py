class Solution:
    def minDeletionSize(self, A):
        x = zip(*A)
        count = 0
        for i in x: #This returns me a tuple of every element in x
            if(list(i)!= sorted(i)): # sorted returns a list
                count += 1
        return count