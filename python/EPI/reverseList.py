from DataStructures.List import List
from DataStructures.NodeList import NodeList



def reverseList(L):
    prev = None
    curr = L

    while(curr):
        nextNode = curr.nextP
        curr.nextP = prev
        prev = curr
        curr = nextNode;

    return prev


L = List()
L.listFromArray([1,2,3,4,5,6])

K = List(reverseList(L.head))

K.printValues()