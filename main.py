# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Model.Order import Order
from Model.Product import Product

# laver et product
prod = Product(1,"hans",123,2,1)
#laver en order
order = Order(1,"12-12-2000",prod,3)

print(order.getOrderId())

p = Product(2,"otto",123,2,1)
p.setName("Ole")
print(p.getName())
