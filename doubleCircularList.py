import os
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

    def graphics(self):
        dot_code = ''
        file = open('reportedot/doubleCircularList.dot', 'w')
        dot_code += '''digraph G {
rankdir=LR;
node [shape = record, height = .1]\n'''
        current = self.head
        counter = 0
        while counter < self.size:
            dot_code+='node'+str(counter)+' [label = "{<f1>|'+str(current.data)+'|<f2>}"];\n}'
            current = current.next
            counter += 1

        counter = 0
        current = self.head
        while counter < self.size-1:
            dot_code += 'node'+str(counter)+':f2 -> node'+str(counter+1)+':f1[dir=both];\n'
            counter += 1
            current = current.next

        dot_code += 'node:f2 -> node'+str(self.size-1)+':f1 [dir=both constraint=false];\n'

        dot_code += "}"

        file.write(dot_code)
        file.close()

        dot_route = 'reportedot/doubleCircularList.dot'
        png_route = 'reportes/doubleCircularList.png'
        command = 'dot -Tpng '+dot_route+' -o '+png_route
        os.system(command)
        routa_out = os.path.abspath(png_route)
        if os.path.isfile(routa_out):
            os.startfile(routa_out)
        else:
            print(f"El archivo {routa_out} no existe.")