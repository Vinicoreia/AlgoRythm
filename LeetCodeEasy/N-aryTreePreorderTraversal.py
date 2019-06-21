class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if(not root):
            return []
        q = collections.deque()
        q.append(root)
        result = []
        while(q):
            result.append(q[0].val)
            node = q[0]
            q.popleft()
            for child in node.children[::-1]:
                q.appendleft(child)
        return result