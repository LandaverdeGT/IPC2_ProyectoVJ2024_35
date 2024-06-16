from tkinter import *
from tkinter import messagebox
from administratorView import AdministratorView

class Login():
    def __init__ (self):
        self.root = Tk()
        self.root.title("Login")
        self.root.geometry("600x400")

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
        global adminWindow
        if self.entry1.get() == "admin" and self.entry2.get() == "admin":
            messagebox.showinfo("Login", "Login exitoso")
            AdministratorView().__init__()
            return True
        elif self.entry1.get() == "" or self.entry2.get() == "":
            messagebox.showerror("Login", "Ingresa un usuario y contraseña")
            return False
        else:
            messagebox.showerror("Login", "Usuario o contraseña incorrectos")
            return False