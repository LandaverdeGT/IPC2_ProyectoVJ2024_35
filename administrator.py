from user import User
class Administrator(User):
    def __init__ (self, id, userName, password, name):
        super().__init__(id, userName, password)
        self.name = name
    
    #Getters and Setters
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name