class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        opened = []
        result = []
        for i in S:
            if i =='(':
                opened.append(i) 
                if len(opened)>1:
                    result.append(i)
            if i == ')':
                if len(opened)>1:
                    result.append(i)
                opened.pop()
        return "".join(result)


# Since the operation of appending to a list is done in O(1) time complexity and the
# pop operation is done is in O(1) time as well.
# So the time complexity for this code is O(n)