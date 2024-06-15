from tkinter import *
from tkinter import messagebox

class AdministratorView():
    def __init__(self):
        self.root = Tk()
        self.root.title("Administrador")
        self.root.geometry("1000X800")

        Button(self.root, text="Cargar Usuarios", width=30, height=5).place(x=50, y=50)
        self.root.mainloop()
    