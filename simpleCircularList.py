import os
from node import Node

class SimpleCircularList():
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
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head
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

    def graphics(self):
        codigo_dot = ''
        archivo = open('reportedot/lista_circular.dot', 'w')
        codigo_dot += '''digraph G {
rankdir=LR;
node [shape = record, height = .1]\n'''

        contador_nodos = 0
        actual = self.head
        while contador_nodos < self.size:
            codigo_dot += 'node'+str(contador_nodos)+' [label = "{'+str(actual.data)+'|<f1>}"];\n'
            actual = actual.next
            contador_nodos += 1

        actual = self.head
        contador_nodos = 0
        while contador_nodos < self.size-1:
            codigo_dot += 'node'+str(contador_nodos)+' -> node'+str(contador_nodos+1)+';\n'
            actual = actual.next
            contador_nodos += 1
        
        codigo_dot += 'node'+str(self.size-1)+' -> node0 [constraint=false];\n'

        codigo_dot += '}'

        archivo.write(codigo_dot)
        archivo.close()

        ruta_dot = 'reportedot/lista_circular.dot'
        ruta_imagen = 'reportes/lista_circular.png'
        comando = 'dot -Tpng '+ruta_dot+' -o '+ruta_imagen
        os.system(comando)

        ruta_reporte2 = os.path.abspath(ruta_imagen)
        os.startfile(ruta_reporte2)