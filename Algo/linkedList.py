class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
    def append(self, value):
        newNode = Node(value)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = newNode
    
    def length(self):
        current = self.head
        count = 0
        while current.next != None:
            count += 1
            current = current.next
        return count

    def printValues(self):
        current = self.head
        while current.next != None:
            current = current.next
            print(str(current.value) + " ")

l = LinkedList()
l.append(1)
l.append(3)
print(l.length())
print(l.printValues())