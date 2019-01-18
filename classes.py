#Classes

class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name 
        self.email = email 
        self.age = age

    def greeting(self):
        return self.name


greet = User('adam', 'adams4lyf@gmail.com', 66)

print(greet.greeting())

#Class Inheritance

class Customer(User):
    
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def getBalance(self):
        return 2345


customer = Customer('chloe','chloe@hotmail.com', 13)
print(customer.name)
print(customer.getBalance())