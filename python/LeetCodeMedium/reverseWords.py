class Solution:
    def reverseWords(self, s: str) -> str:
        a  = s.split(' ')
        
        a =  [x for x in a[::-1] if x]
        return " ".join(a)