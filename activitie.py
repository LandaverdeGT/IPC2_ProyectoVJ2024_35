class Activitie():
    def __init__(self, id, name, description, employee, day, hour):
        self.id = id
        self.name = name
        self.description = description
        self.employee = employee
        self.day = day
        self.hour = hour
    
    def __str__(self):
        return f'''
        ID: {self.id}
        Nombre: {self.name}
        Descripción: {self.description}
        Empleado: {self.employee}
        Día: {self.day}
        Hora: {self.hour}
        '''
    
    #Getters and Setters
    def getID(self):
        return self.id
    def setID(self, id):
        self.id = id
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getDescription(self):
        return self.description
    def setDescription(self, description):
        self.description = description
    def getEmployee(self):
        return self.employee
    def setEmployee(self, employee):
        self.employee = employee
    def getDay(self):
        return self.day
    def setDay(self, day):
        self.day = day
    def getHour(self):
        return self.hour
    def setHour(self, hour):
        self.hour = hour
        