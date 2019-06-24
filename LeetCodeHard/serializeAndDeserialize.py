class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        bTree =  []
        if(not root ):
            return str([])
        q = collections.deque()
        q.append(root)
        bTree.append(q[0].val)
        while(q):
            node = q.popleft()
            if(node.left):
                q.append(node.left)
                bTree.append(node.left.val)
            else:
                bTree.append(None)
            if(node.right):
                q.append(node.right)
                bTree.append(node.right.val)
            else:
                bTree.append(None)
                
        return str(bTree)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        bTree = eval(data)
        if bTree == []:
            return []
        root = TreeNode(bTree[0])
        q = collections.deque()
        q.append(root)
        i = 1
        while(q):
            node = q.popleft()
            if(bTree[i] != None):
                left = TreeNode(bTree[i])
                node.left = left
                q.append(left)
            if(bTree[i+1] != None):
                right = TreeNode(bTree[i+1])
                q.append(right)
                node.right = right
            i+=2
        return root
