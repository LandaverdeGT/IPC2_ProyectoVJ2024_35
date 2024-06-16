from tkinter import *
from tkinter import messagebox
from xmlFunctions import XMLFunctions
from doubleCircularList import DoubleCircularList

route = ''
list = DoubleCircularList()

class AdministratorView():
    def __init__(self):
        global list
        self.root = Tk()
        self.root.title("Administrador")
        self.root.geometry("1000x400")
        self.root.positionfrom("user")
        #Titulos
        Label(self.root, text="Cargar Archivos").place(x=50, y=20)
        Label(self.root, text="Generar Reportes").place(x=250, y=20)
        #Botones
        Button(self.root, text="Cargar Usuarios", width=20, height=5, command=self.Load_XML).place(x=50, y=40)
        Button(self.root, text="Imprimir Usuarios", width=20, height=5, command=self.Read_XML).place(x=50, y=150)
        Button(self.root, text="Generar Reporte de Productos", width=20, height=5, command=self.graphic).place(x=500, y=40)
        
        self.root.mainloop()
        
    def Load_XML(self):
        global route
        route = XMLFunctions.Load_XML()
        print(route)
        
    def Read_XML(self):
        list = XMLFunctions.Read_XML(route)
        list.printList()

    def graphic(self):
        list.graphics()

    