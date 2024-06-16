import xml.etree.ElementTree as ET
from tkinter import filedialog, messagebox
from client import Client
from doubleList import DoubleList
from simpleCircularList import SimpleCircularList 
from doubleCircularList import DoubleCircularList
from product import Product
from employee import Employee

#Instancia de las listas
list = DoubleList()
circularList = SimpleCircularList()
doubleCircularList = DoubleCircularList()

class XMLFunctions():
    def Load_XML():
        global ruta
        ruta_xml = filedialog.askopenfilename(title="Cargar Archivo XML", filetypes=(('Text files', '*.xml'), ('All files', '*.*')))
        ruta = ruta_xml
        return ruta_xml
    
    def Read_XML(ruta_xml):
        global list
        global circularList
        global doubleCircularList
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
                        case "correo":
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
                if len(phone <8):
                    messagebox.showerror("Error", "El número de teléfono debe tener al menos 8 dígitos")
                elif not ("@gmail.com" in email):
                    messagebox.showerror("Error", "El correo no contiene la estructura correcta")
                else:
                    newClient = Client(id, userName, password, name, age, email, phone)
                    if not list.find_user(id):
                        list.insert(newClient)
                    else:
                        messagebox.showerror("Error", "El usuario ya existe")
            return list
        elif root.tag == "productos":
            for producto in root:
                id = producto.attrib['id']
                name = ""
                price = ""
                description = ""
                category = ""
                quanty = ""
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
                    print(f'''
                    ID: {id}
                    Nombre: {name}
                    Precio: {price}
                    Descripción: {description}
                    Categoría: {category}
                    Cantidad: {quanty}
                    ''')
                    print("-------------------------------------------------")
                    try:
                        price = float(price)
                        quanty = int(quanty)
                        newProduct = Product(id, price, description, category, quanty, name)
                        if not doubleCircularList.findElement(id):
                            doubleCircularList.insert(newProduct)
                        else:
                            messagebox.showerror("Error", "El producto ya existe")
                    except:
                        messagebox.showerror("Error", "El precio y la cantidad deben ser números")
        elif root.tag == "empleados":
            for empleado in root:
                code = empleado.attrib['codigo']
                password = empleado.attrib['password']
                name = ""
                job = ""
                for subempleado in empleado:
                    match subempleado.tag:
                        case "codigo":
                            code = subempleado.text
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
                    newEmployee = Employee(code, userName, password, name, job)
                    circularList.insert(newEmployee)
                else:
                    messagebox.showerror("Error", "El empleado ya existe")
            return circularList
            



        