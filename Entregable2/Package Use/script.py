# Import the package ecommerce and its modules
from ecommerce.Client import Client as Client
from ecommerce.Product import Product as Product
from ecommerce.Person import Person as Person
from ecommerce.Cart import Cart as Cart

# Create 3 clients
client1 = Client('John', 'Doe', 30, 'Calle 1', '123456789', 'john@doe.com', '9940194', '1')
client2 = Client('Jane', 'Doe', 30, 'Calle 1', '123456789', 'jane@doe.com', '1234213', '2')
client3 = Client('James', 'Smith', 30, 'Calle 1', '123456789', 'james@smith,com', '1234213', '3')

# Make clients greet
client1.greet()
client2.greet()

# Create 3 products
product1 = Product('Laptop', 10, 3)
product2 = Product('Phone', 20, 15)
product3 = Product('Tv', 30, 2)

# Create 3 carts
cart1 = Cart()
cart2 = Cart()
cart3 = Cart()

# Add products to carts
cart1.add(product1)
cart1.add(product2)
cart2.add(product3)
cart3.add(product1)

# Create people to show inheritance
person1 = Person('Adam', 'Johnson', 30, 'Calle 1', '123456789', 'adam@johnson.com', 'asdfas244')
person1.greet()

# Print carts
print(cart1)
print(cart2)
print(cart3)
