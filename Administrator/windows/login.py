from tkinter import *
from tkinter import messagebox

class Login():
    def __init__ (self):
        self.root = Tk()
        self.root.title("Login")
        self.root.geometry("600x400")

        global entry1
        global entry2
        Label(self.root, text="Usuario").place(x=100, y=50)
        Label(self.root, text="Contraseña").place(x=100, y=100)

        self.entry1 = Entry(self.root, width=50)
        self.entry1.place(x=200, y=50)
        self.entry2 = Entry(self.root, show="*", width=50)
        self.entry2.place(x=200, y=100)

        Button(self.root, text="Login", command=self.Login, width=20, height=3).place(x=200, y=250)
        self.root.mainloop()

    def Login(self):
        if self.entry1.get() == "admin" and self.entry2.get() == "admin":
            messagebox.showinfo("Login", "Login exitoso")
            return True
        elif self.entry1.get() == "" or self.entry2.get() == "":
            return False
            messagebox.showerror("Login", "Ingrese usuario y contraseña")
        else:
            return False
            messagebox.showerror("Login", "Usuario o contraseña incorrectos")