from node import Node

class SimpleCircularList():
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def insert(self, data):
        newNode = Node(data)
        if self.head == None and self.last == None:
            self.head = newNode
            self.last = newNode
            self.last.next = self.head
        else:
            self.last.next = newNode
            newNode.next = self.head
            self.last = newNode
        self.size += 1

    def printList(self):
        if self.head == None:
            print("Lista vacía")
        else:
            current = self.head
            counter = 0
            while counter < self.size:
                print(current.data)
                current = current.next
                counter += 1

    def findEmployee(self, code):
        find = False
        current = self.head
        counter = 0
        while counter < self.size:
            if current.data.id == code:
                find = True
                break
            current = current.next
            counter += 1
        return find

