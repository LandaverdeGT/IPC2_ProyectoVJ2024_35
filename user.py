class User():
    def __init__ (self, id, password):
        self.id = id
        self.password = password
    
    #Getters and Setters
    def getID(self):
        return self.id
    def setID(self, id):
        self.id = id

    def getPassword(self):
        return self.password
    def setPassword(self, password):
        self.password = password

    def __str__(self):
        return f'''
        ID: {self.id}
        Contraseña: {self.password}
        '''