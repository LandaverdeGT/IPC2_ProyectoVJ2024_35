from tkinter import *
from tkinter import messagebox

class ActivitiesOfDay():
    def __init__(self, text):
        self.root = Tk()
        self.root.title("Actividades del Día de Hoy")
        self.root.geometry("600x400")
        
        Label(self.root, text="Actividades del Día de Hoy").place(x=200, y=10)
        
        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.Activites = Text(self.root, width=100, height=100, yscrollcommand=scrollbar.set)
        self.Activites.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=self.Activites.yview)

        self.Activites.insert(END, text)

        self.root.mainloop()