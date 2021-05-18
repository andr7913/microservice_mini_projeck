# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Model.Product import Product
from Model.Order import Order

p1 = Product()
print(p1.Name)

order = Order()
print(order.OrderId)

p = Product()
p.setName("Ole")
print(p.getName())
