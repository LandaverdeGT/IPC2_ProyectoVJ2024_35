from nodeDouble import Node

class DoubleCircularList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def insert(self, data):
        newNode = Node(data)
        if self.head == None and self.tail == None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.tail.next = self.head
            self.head.prev = self.tail
        self.size += 1

    def printList(self):
        if self.head == None:
            print("Lista Vacía")
        else:
            current = self.head
            counter = 0
            while counter < self.size:
                print(current.data)
                current = current.next
                counter += 1

    def findElement(self, id):
        find = False
        current = self.head
        counter = 0
        while counter < self.size:
            if current.data.id == id:
                find = True
                break
            current = current.next
            counter += 1
        return find
