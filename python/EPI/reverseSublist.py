from DataStructures.List import List
from DataStructures.NodeList import NodeList

# Write a program that takes a single Linked list L and two integers s and f as arguments and reverses the order
# of the nodes between s and f, inclusive. Do not allocate aditional nodes. Also indexing starts at 1.


def reverseSublist(L, s, f):
    dummy_head = prev = NodeList(0, L)

    for _ in range(1, s):
        prev = prev.nextP
    # Now sublist_head is pointing to the first element

    curr = prev.nextP #first element of the sublist to be reversed

    for _ in range(f-s):
        nextNode = curr.nextP
        curr.nextP =  nextNode.nextP
        nextNode.nextP = prev.nextP
        prev.nextP = nextNode

    return dummy_head.nextP

L = List()
L.listFromArray([1,2,3,4,5])
K = List(reverseSublist(L.head, 2, 4))
# K.printValues()