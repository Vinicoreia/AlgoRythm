from NodeList import NodeList


class List:
    def __init__(self, head=None):
        self.head = NodeList()

    def listFromArray(self, arr):
        newNode = NodeList()
        head = currentNode = self.head
        for i in arr:
            currentNode.nextP = NodeList(i)
            currentNode = currentNode.nextP
        self.head = head.nextP

    def printValues(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.nextP

    def length(self):
        currentNode = self.head
        count = 0
        while currentNode:
            count += 1
            currentNode = currentNode.nextP
        return count

    def append(self, value):
        currentNode = self.head
        while(currentNode.nextP):
            currentNode = currentNode.nextP
        currentNode.nextP = NodeList(value)
