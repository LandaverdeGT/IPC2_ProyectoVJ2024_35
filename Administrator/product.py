class Product():
    def __init__ (self, id, price, description, category, quanty, image):
        self. id = id
        self.price = price
        self.description = description
        self.category = category
        self.quanty = quanty
        self.image = image

    #Getters and Setters
    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id
    
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price

    def getDescription(self):
        return self.description
    def setDescription(self, description):
        self.description = description

    def getCategory(self):
        return self.category
    def setCategory(self, category):
        self.category = category

    def getQuanty(self):
        return self.quanty
    def setQuanty(self, quanty):
        self.quanty = quanty

    def getImage(self):
        return self.image
    def setImage(self, image):
        self.image = image
        