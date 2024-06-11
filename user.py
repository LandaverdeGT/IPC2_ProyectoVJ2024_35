class User():
    def __init__ (self, id, userName, password):
        self.id = id
        self.userName = userName
        self.password = password
    
    #Getters and Setters
    def getID(self):
        return self.id
    def setID(self, id):
        self.id = id
    
    def getUserName(self):
        return self.userName
    def setUserName(self, userName):
        self.userName = userName

    def getPassword(self):
        return self.password
    def setPassword(self, password):
        self.password = password