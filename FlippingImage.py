class Solution:
    def flipAndInvertImage(self, A):
        result = []
        for l in A:
            result.append([1 if i==0 else 0 for i in l[::-1]])
        return result