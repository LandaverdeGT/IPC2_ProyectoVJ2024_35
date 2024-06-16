from user import User

class Client(User):
    def __init__ (self, id, password, name, age, email, phone):
        super().__init__(id, userName, password)
        self.name = name
        self.age = age
        self.phone = phone

    def __str__(self):
        return f'''
        ID: {self.id}
        Contraseña: {self.password}
        Nombre: {self.name}
        Edad: {self.age}
        Correo: {self.email}
        Telefono: {self.phone}
        '''

    #Getters and Setters
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age
    def setAge(self, age):
        self.age = age

    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email = email

    def getPhone(self):
        return self.phone
    def setPhone(self, phone):
        self.phone = phone