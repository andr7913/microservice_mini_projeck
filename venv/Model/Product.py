class Product:

  def __init__(self):
    self.productId=0
    self.Name = "hans"
    self.Price = 1
    self.ItemsInStock = 2
    self.ItemsReserved = 1

  def setProductID(self, id):
    self.productId=id

  def getProductID(self):
     return self.productId

  def setName(self, name):
    self.Name = name

  def getName(self):
     return self.Name

  def setPrice(self, price):
     self.Price = price

  def getPrice(self):
     return self.Price

  def setItemsInStock(self, ItemsInStock):
     self.ItemsInStock = ItemsInStock

  def getItemsInStock(self):
     return self.ItemsInStock


  def setItemsReserved(self, ItemsReserved):
     self.ItemsReserved = ItemsReserved


  def getItemsReserved(self):
     return self.ItemsReserved
