from user import User

class Client(User):
    def __init__ (self, id, userName, password, name, age, email, phone):
        super().__init__(id, userName, password)
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

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