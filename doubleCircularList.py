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
        codigodot = ''
        archivo = open('reportedot/lista_doble_circular.dot', 'w')
        codigodot+= '''digraph G {
  rankdir=LR;
  node [shape = record, height = .1]\n'''
        #PRIMERO CREAMOS LOS NODOS
        actual = self.head
        contador = 0
        while contador < self.size:
            codigodot+='node'+str(contador)+' [label = "{<f1>|'+str(actual.data)+'|<f2>}"];\n'
            actual = actual.next
            contador += 1

        #AHORA CREAMOS LOS APUNTADORES
        contador = 0
        actual = self.head
        while contador < self.size-1:
            codigodot += 'node'+str(contador)+':f2  -> node'+str(contador+1)+':f1[dir=both];\n'
            contador += 1
            actual = actual.next
        
        #CREAMOS LOS APUNTADORES DE LOS EXTREMOS
        codigodot += 'node0:f1 -> node'+str(self.size-1)+':f2 [dir=both constraint=false];\n'

        codigodot += '}'

        #ESCRIBIR EL ARCHIVO .DOT
        archivo.write(codigodot)
        archivo.close()

        #GENERAMOS LA IMAGEN
        ruta_dot = 'reportedot/lista_doble_circular.dot'
        ruta_png = 'reportes/lista_doble_circular.png'
        comando = 'dot -Tpng '+ruta_dot+' -o '+ruta_png
        os.system(comando)

        #ABRIMOS LA IMAGEN
        #convierte la ruta relativa a absoluta
        ruta_salida = os.path.abspath(ruta_png)
        os.startfile(ruta_salida)