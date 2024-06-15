from node import Node

class DoubleList():
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, data):
        new_node = Node(data)
        current = self.head
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            if self.tail.next == None:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
        self.size += 1

    def printList(self):
        if self.head == None:
            print("Lista vacía")
        else:
            current = self.head
            while current != None:
                print(current.data)
                current = current.next