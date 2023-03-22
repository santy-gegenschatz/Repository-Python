class Person():
    def __init__(self, name, surname, age, address, phone, email, password):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f'Name: {self.name} Surname: {self.surname} Age: {self.age} Address: {self.address} Phone: {self.phone} Email: {self.email} Password: {self.password}'
    
    def greet(self):
        print(f'Hello, my name is {self.name}. Nice to meet you!')