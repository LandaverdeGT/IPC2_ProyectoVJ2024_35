import xml.etree.ElementTree as ET
from tkinter import filedialog, messagebox
from doubleList import DoubleList
from simpleCircularList import SimpleCircularList 
from doubleCircularList import DoubleCircularList
from client import Client
from product import Product
from employee import Employee
from activitie import Activitie
from matrizDispersa import MatrizDispersa

#Instancia de las listas
listSimple = DoubleList()
circularList = SimpleCircularList()
doubleCircularList = DoubleCircularList()
matriz = MatrizDispersa()

class XMLFunctions():
    def Load_XML():
        global ruta
        ruta_xml = filedialog.askopenfilename(title="Cargar Archivo XML", filetypes=(('Text files', '*.xml'), ('All files', '*.*')))
        ruta = ruta_xml
        return ruta_xml
    
    def Read_XML(ruta_xml):
        global listSimple
        global circularList
        global doubleCircularList
        global matriz
        tree = ET.parse(ruta_xml)
        root = tree.getroot()
        userName = ""
        print(root.tag)
        if root.tag == "usuarios":
            for usuario in root:
                id = usuario.attrib['id']
                password = usuario.attrib['password']
                name = ""
                age = ""
                email = ""
                phone = ""
                for subusuario in usuario:
                    match subusuario.tag: 
                        case "nombre": 
                            name = subusuario.text
                        case "edad":
                            age = subusuario.text
                        case "email":
                            email = subusuario.text
                        case "telefono":
                            phone = subusuario.text
                print(f'''
                ID: {id}
                Nombre: {name}
                Edad: {age}
                Correo: {email}
                Telefono: {phone}
                    ''')
                print("-------------------------------------------------")
                if len(phone)>8:
                    messagebox.showerror("Error", "El número de teléfono debe tener al menos 8 dígitos")
                elif not email.__contains__("@") or not email.__contains__(".com"):
                    messagebox.showerror("Error", "El correo no es válido")
                else:
                    newClient = Client(id, password, name, age, email, phone)
                    if not listSimple.find_user(id):
                        listSimple.insert(newClient)
                    else:
                        messagebox.showerror("Error", "El usuario ya existe")
            return listSimple
        elif root.tag == "productos":
            for producto in root:
                id = producto.attrib['id']
                name = ""
                price = ""
                description = ""
                category = ""
                quanty = ""
                image = ""
                for subproducto in producto:
                    match subproducto.tag:
                        case "nombre":
                            name = subproducto.text
                        case "precio": 
                            price = subproducto.text
                        case "descripcion":
                            description = subproducto.text
                        case "categoria":
                            category = subproducto.text
                        case "cantidad":
                            quanty = subproducto.text
                        case "imagen":
                            image = subproducto.text
                print(f'''
                ID: {id}
                Nombre: {name}
                Precio: {price}
                Descripción: {description}
                Categoría: {category}
                Cantidad: {quanty}
                Imagen: {image}
                ''')
                print("-------------------------------------------------")
                if not doubleCircularList.findElement(id):
                    price = float(price)
                    quanty = int(quanty)
                    newProduct = Product(id, name, price, description, category, quanty, image)
                    doubleCircularList.insert(newProduct)
                else:
                    messagebox.showerror("Error", "El producto ya existe")
            return doubleCircularList
        elif root.tag == "empleados":
            for empleado in root:
                code = empleado.attrib['codigo']
                password = ""
                name = ""
                job = ""
                for subempleado in empleado:
                    match subempleado.tag:
                        case "nombre":
                            name = subempleado.text
                        case "puesto":
                            job = subempleado.text
                print(f'''
                Código: {code}
                Nombre: {name}
                Puesto: {job}
                ''')
                if not circularList.findEmployee(code):
                    newEmployee = Employee(code, password, name, job)
                    circularList.insert(newEmployee)
                else:
                    messagebox.showerror("Error", "El empleado ya existe")
            return circularList
        elif root.tag == "actividades":
            for actividad in root:
                id = actividad.attrib['id']
                name = ""
                description = ""
                employee = ""
                day = ""
                hour = ""
                for subactividad in actividad:
                    match subactividad.tag:
                        case "nombre":
                            name = subactividad.text
                        case "descripcion":
                            description = subactividad.text
                        case "empleado":
                            employee = subactividad.text
                        case "dia":
                            day = subactividad.text
                            hour = subactividad.attrib['hora']
                        
                print(f'''
                ID: {id}
                Nombre: {name}
                Descripción: {description}
                Empleado: {employee}
                Día: {day}
                Hora: {hour}
                ''')
                print("-------------------------------------------------")
                newActivitie = Activitie(id, name, description, employee, day, hour)
                hour = int(hour)
                day = int(day)
                matriz.insertar(hour, day, newActivitie)
            return matriz



        