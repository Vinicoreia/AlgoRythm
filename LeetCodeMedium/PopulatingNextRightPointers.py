class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if(not root):
            return
        
        
        q = collections.deque()
        q.append([0,root])
        root.next = None
        prev = [-1,None]
        while(q):
            node = q.popleft()
            if(node[0] ==prev[0]):
                prev[1].next = node[1]
            if(node[1].left):
                q.append([node[0]+1, node[1].left])
            if(node[1].right):
                q.append([node[0]+1, node[1].right])
            prev = node
        return root