from node import Node

class SimpleList():
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def insert(self, data):
        newNode = Node(data)
        current = self.head
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current != None:
                if current.next == None:
                    current.next = newNode
                    break
                current = current.next
        self.size += 1
