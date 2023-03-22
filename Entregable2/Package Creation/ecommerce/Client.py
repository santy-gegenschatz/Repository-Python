from .Person import *

class Client(Person):
    # Must have a minimum of 4 attributes and 2 methods
    def __init__(self, name, surname, age, address, phone, email, password, client_id):
        super().__init__(name, surname, age, address, phone, email, password)
        self.client_id = client_id

    def __str__(self):
        return f'Name: {self.name} Surname: {self.surname} Age: {self.age} Address: {self.address} Phone: {self.phone} Email: {self.email} Password: {self.password} Client ID: {self.client_id}'
    
    # Methods
    def greet(self):
        print(f'Hello, my name is {self.name} and I am a client. Hope to keep buying!')

    def buy(self, product):
        print(f'Buying {product}. The total is {product.price}')