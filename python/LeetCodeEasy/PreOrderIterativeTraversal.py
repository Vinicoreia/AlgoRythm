import collections
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root):
        if not root:
            return []
        q = collections.deque() #This will serve as an abstraction of a stack
        q.append(root)
        result = []
        while(q): # while q not empty
            result.append(q[0].val)
            node = q[0] # representation of the subtree been Traversed at the moment
            q.popleft()
            for child in node.children[::-1]: #Since i want to stack them i must go in the -1 direction
                q.appendleft(child)
            return result