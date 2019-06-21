#Calculate the maxDepth of an N-ary Tree

import collections
class Solution:
    def maxDepth(self, root):
        if(not root):
            return 0
        q = collections.deque()
        depth = 1
        q.append([root, depth]) #Depth keeps the state of which depth we are
        while(q):
            node = q.pop()
            for child in node[0].children:
                q.appendleft([child, node[1]+1]) #this way we only add once the depth state
            depth = node[1]
        return depth