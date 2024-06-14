from employee import Employee

class Administrator(Employee):
    def __init__ (self, id, userName, password, name, job):
        super().__init__(id, userName, password, name)
        self.job = job
    
    #Getters and Setters
    def getJob(self):
        return self.job
    def setJob(self, job):
        self.job = job