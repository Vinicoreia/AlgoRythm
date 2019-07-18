class Solution:
    def commonChars(self, A):
        splitted = []
        for n in A[1:]:
            splitted.append(list(n))
        result = []
        for letter in A[0]:
            letterIn = True
            for s in splitted:
                if(letter in s)
                    s[s.index(letter)] = None
                else:
                    letterIn = False
                    break
            if(letterIn==True):
                result.append(letter)
        return result