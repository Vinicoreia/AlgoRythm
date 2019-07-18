import collections
class Solution:
    def isUnivalTree(self, root):
        val = 0
        if(root):
            val = root.val
        
        q =  collections.deque()
        q.append(root)

        while(q):
            node = q.popleft()
            if(node and node.val != val):
                return False
            else:
                if (node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
        return True
