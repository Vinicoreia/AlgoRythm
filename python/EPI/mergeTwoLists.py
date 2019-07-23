from DataStructures.NodeList import NodeList


L1 = NodeList(2)
L1.nextP = NodeList(5)
L1.nextP.nextP = NodeList(7)

L2 = NodeList(3)
L2.nextP = NodeList(11)
 
def printList(L):
    while(L):
        print(L.data)
        L = L.nextP

def mergeTwoLists(L1, L2):
    dummyhead = merging = NodeList()

    while(L1 and L2):
        if(L1.data < L2.data):
            merging.nextP = L1
            L1 = L1.nextP
        else:
            merging.nextP =  L2
            L2 = L2.nextP

        merging = merging.nextP
    merging.nextP = L1 or L2
    
    return dummyhead.nextP


printList(mergeTwoLists(L1, L2))