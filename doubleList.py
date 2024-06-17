import os
from nodeDouble import Node

class DoubleList():
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

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

    def search(self, id):
        find = False
        current = self.head
        while current != None:
            if current.data.id == id:
                find = True
                break
            current = current.next
        return find
    
    def printList(self):
        if self.head == None:
            return ("Lista vacía")
        else:
            current = self.head
            while current != None:
                print(current.data)
                current = current.next

    def find_user(self, id):
        findUser = False
        current = self.head
        while current != None:
            if current.data.id == id:
                findUser = True
                break
            current = current.next
        return findUser

    def graphics(self):
        dot_code = ''
        file = open('reportedot/doubleList.dot', 'w')
        dot_code += '''digraph G {
rankdir=LR;
node [shape = record, height = .1]\n'''
        current = self.head
        counter = 0
        while current != None:
            dot_code+='node'+str(counter)+' [label = \"{<f1>|'+str(current.data)+'|<f2>}"];\n'
            counter += 1
            current = current.next

        current = self.head
        counter = 0
        while current.next != None:
            dot_code += 'node'+str(counter)+':f2 -> node'+str(counter+1)+':f1;\n'
            dot_code += 'node'+str(counter+1)+':f1 -> node'+str(counter)+':f2;\n'
            counter += 1
            current = current.next
            
        dot_code += '}'

        file.write(dot_code)
        file.close()

        dot_route = 'reportedot/doubleList.dot'
        png_route = 'reportes/ListaUsuarios.png'
        command = 'dot -Tpng '+dot_route+' -o '+png_route
        os.system(command)

        final_route = os.path.abspath(png_route)
        os.startfile(final_route)
