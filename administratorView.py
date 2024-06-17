import datetime
from tkinter import *
from tkinter import messagebox
from xmlFunctions import XMLFunctions
from activitiesOfDay import ActivitiesOfDay

route = ''
list = ''
class AdministratorView():
    def __init__(self):
        global list
        self.root = Tk()
        self.root.title("Administrador")
        self.root.geometry("800x1000")
        self.root.positionfrom("user")
        #Titulos
        lblArchivos = Label(self.root, text="Cargar Archivos").place(x=60, y=20)
        lblReportes = Label(self.root, text="Generar Reportes").place(x=260, y=20)
        lblAutorizarCompra = Label(self.root, text="Autorizar Compra").place(x=200, y=275)
        #Botones
        btnSalir = Button(self.root, text="Salir", width=20, height=2, command=self.root.destroy).place(x=500, y=10)
        btnCargarUsuarios = Button(self.root, text="Cargar Usuarios", width=20, height=2, command=self.Load_XML).place(x=50, y=40)
        btnCargarProductos = Button(self.root, text="Cargar Productos", width=20, height=2, command=self.Load_XML).place(x=50, y=90)
        btnCargarEmpleados = Button(self.root, text="Cargar Empleados", width=20, height=2, command=self.Load_XML).place(x=50, y=140)
        btnCargarActividades = Button(self.root, text="Cargar Actividades", width=20, height=2, command=self.Load_XML).place(x=50, y=190)
        btnGenerarReporteUsuarios = Button(self.root, text="Generar Reporte de Usuarios", width=25, height=2, command=self.graphic).place(x=240, y=40)
        btnGenerarReporteProductos = Button(self.root, text="Generar Reporte de Productos", width=25, height=2, command=self.graphic).place(x=240, y=90)
        btnGenerarReporteEmpleados = Button(self.root, text="Generar Reporte de Empleados", width=25, height=2, command=self.graphic).place(x=240, y=140)
        btnGenerarReporteActividades = Button(self.root, text="Generar Reporte de Actividades", width=25, height=2, command=self.graphic).place(x=240, y=190)
        btnVerActividadesdeHoy = Button(self.root, text="Ver Actividades de Hoy", width=25, height=2, command=self.activitiesOfDay).place(x=500, y=300)
        
        btnAceptar = Button(self.root, text="Login", width=20, height=2).place(x=600, y=500)
        btnRechazar = Button(self.root, text="Rechazar", width=20, height=2).place(x=600, y=550)
        
        self.root.mainloop()
        
    def Load_XML(self):
        global route
        global list
        route = XMLFunctions.Load_XML()
        print(route)
        list = XMLFunctions.Read_XML(route)
        #list.printList()
        
    def graphic(self):
        global list
        list.graphics()

    def activitiesOfDay(self):
        today = datetime.datetime.today()
        today_day = today.weekday()+1
        intToday = int(today_day)
        data = list.recorridoColumnas(intToday)
        print("Datos Obtenidos: ", data)
        activitiesWindow = ActivitiesOfDay(data)
