class Solution:
    def hammingDistance(self, x, y):
        a = x^y
        return bin(a).count("1")

    # This is a simple XOR operation
    # if the bytes are different then returns 1, else return 0