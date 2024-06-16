from tkinter import *
from tkinter import messagebox
from xmlFunctions import XMLFunctions

route = ''
class AdministratorView():
    def __init__(self):
        self.root = Tk()
        self.root.title("Administrador")
        self.root.geometry("1000x400")
        self.root.positionfrom("user")
        #Titulos
        Label(self.root, text="Menú Administrador").place(x=400, y=10)

        #Botones
        Button(self.root, text="Cargar Usuarios", width=30, height=5, command=self.Load_XML).place(x=50, y=50)
        Button(self.root, text="Imprimir Usuarios", width=30, height=5, command=self.Read_XML).place(x=50, y=150)
        self.root.mainloop()
        
    def Load_XML(self):
        global route
        route = XMLFunctions.Load_XML()
        print(route)
        
    def Read_XML(self):
        list = XMLFunctions.Read_XML(route)
        list.printList()