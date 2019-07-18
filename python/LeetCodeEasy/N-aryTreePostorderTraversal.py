"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        q =  collections.deque()
        result  = []
        q.append(root)
        while(q):
            result.append(q[0].val)
            node = q[0]
            q.pop()
            for i in node.children[::-1]:
                q.append(i)
        return result[::-1]
            