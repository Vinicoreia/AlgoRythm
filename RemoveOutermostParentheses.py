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


# ((()))