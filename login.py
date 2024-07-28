from tkinter import *
from tkinter import messagebox
from administratorView import AdministratorView
from doubleList import DoubleList

list = DoubleList()

class Login():
    def __init__ (self):
        self.root = Tk()
        self.root.title("Login")
        self.root.geometry("600x400")
        self.root.config(bg="sky blue")

        global entry1
        global entry2
        Label(self.root, text="IPC2Market").place(x=200, y=10)
        Label(self.root, text="Usuario").place(x=100, y=50)
        Label(self.root, text="Contraseña").place(x=100, y=100)

        self.entry1 = Entry(self.root, width=50)
        self.entry1.place(x=200, y=50)
        self.entry2 = Entry(self.root, show="*", width=50)
        self.entry2.place(x=200, y=100)

        Button(self.root, text="Login", command=self.LoginValidate, width=20, height=3).place(x=200, y=250)
        self.root.mainloop()

    def LoginValidate(self):
        global list
        global adminWindow
        if self.entry1.get() == "AdminIPC2" and self.entry2.get() == "IPC2VJ2024":
            messagebox.showinfo("Login", "Login exitoso")
            AdministratorView()
            return True
        elif self.entry1.get() == "" or self.entry2.get() == "":
            messagebox.showerror("Login", "Ingresa un usuario y contraseña")
            return False
        else:
            messagebox.showerror("Login", "Usuario o contraseña incorrectos")
            return False