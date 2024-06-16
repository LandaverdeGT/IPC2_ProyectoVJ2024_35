from user import User

class Employee(User):
    def __init__ (self, id, password, name, job):
        super().__init__(id, password, name)
        self.job = job
    
    def __str__(self):
        return f'''
        ID: {self.id}
        Contraseña: {self.password}
        Nombre: {self.name}
        Puesto: {self.job}
        '''
    
    #Getters and Setters
    def getJob(self):
        return self.job
    def setJob(self, job):
        self.job = job