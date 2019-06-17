import queue
class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

a = Node(10)
a.right = Node(2)
a.left = Node(3)
a.right.right = Node(5)
a.right.left = Node(1)
a.left.right =  Node(100)
a.left.left = Node(6)



def BFS(c):
    Q = queue.Queue()
    Q.put(c)
    while(not Q.empty()):
        p = Q.get()
        print(p.value)
        if(p.left != None):
            Q.put(p.left)
        if(p.right != None):
            Q.put(p.right)

def PreOrder(c):
    if(c == None):
        return
    else:
        print(c.value)
        PreOrder(c.left)
        PreOrder(c.right)

def PostOrder(c):
    if(c==None):
        return
    else:
        PostOrder(c.left)
        PostOrder(c.right)
        print(c.value)

def InOrder(c):
    if(c==None):
        return
    else:
        InOrder(c.left)
        print(c.value)
        InOrder(c.right)