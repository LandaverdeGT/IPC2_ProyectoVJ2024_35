from node_double import NodeDouble

class DoubleList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def insert(self, data):
        newNode = NodeDouble(data)
        if self.head == None and self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.size += 1

    def printList(self):
        if self.head == None:
            print("Lista vacía")
        else:
            current = self.head
            while current != None:
                print(current.data)
                current = current.next