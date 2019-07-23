from DataStructures.NodeList import NodeList
from typing import List

def arrayToLinkedList(A):
    dummyHead = L = NodeList()
    for i in A:
        L.nextP = NodeList()
        L = L.nextP
        L.data = i
    return dummyHead.nextP


L1 = arrayToLinkedList([1,2,3,4])

while(L1):
    print(L1.data)
    L1 = L1.nextP
