#Key Concepts:

#Class: 'A blueprint or template for creating objects. It defines attributes (variables) and methods (functions) that the objects created from the class will have.'

#Object: ' An instance of a class. When a class is defined, no memory is allocated until an object is created from it.'

#Attributes: ' Variables that belong to the class. They represent the state or data of an object.'

#Methods: 'Functions defined inside the class. They describe the behaviors/actions that the objects of the class can perform.'

#Constructor: ' A special method called __init__ that is automatically invoked when a new object of the class is created. It's used for initializing the object's attributes.'

#Example: Defining a Class and Creating Objects
""" 
class Car:
    # Constructor to initialize the attributes of the class
    def __init__(self, make, model, year):
        self.make = make  # Attribute of the class
        self.model = model
        self.year = year

    # Method to display the car details
    def car_info(self):
        return f"{self.year} {self.make} {self.model}"

    # Method to simulate driving the car
    def drive(self):
        return f"{self.make} {self.model} is now driving."

# Creating an object of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Accessing the object's attributes and methods
print(my_car.car_info())  # Output: 2020 Toyota Camry
print(my_car.drive())      # Output: Toyota Camry is now driving. 

"""
#Explanation:
""" 
Class Car is defined with attributes (make, model, year) and methods (car_info, drive).
__init__ constructor initializes the object with the provided values.
my_car is an object (or instance) of the Car class.
Methods are called on the object to perform actions.
Would you like to explore more advanced topics, like inheritance, polymorphism, or practice with some exercises? 
"""

                                      #Exersises for classes and object

#Exercise 1: Person Class
""" 
Question:
Create a class Person with:

Attributes: name, age
Method: greet() that prints "Hello, my name is [name] and I am [age] years old." 
"""
""" 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an object of Person
p1 = Person("Alice", 25)
p1.greet()  # Output: Hello, my name is Alice and I am 25 years old.
"""

#Exercise 2: Car Class

""" 
Create a class Car with:

Attributes: make, model, year
Methods:
start() - Prints "The [make] [model] is starting."
stop() - Prints "The [make] [model] is stopping." 
"""

""" 
class car:
    def __init__(self,make,model,year) :
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print(f"The {self.make} {self.model} is starting in {self.year}.")    
    def stop(self):
        print(f"The {self.make} {self.model} is stopping.")      
obj=car("Toyota", "Corolla", 2020) 
obj.start()
obj.stop() 
"""      
#output:
#The Toyota Corolla is starting in 2020.
#The Toyota Corolla is stopping

#Exercise 3: Book Class
""" 
Create a class Book with:
Attributes: title, author, price
Methods:
get_info() - Returs "Title: [title], Author: [author], Price: $[price]"
apply_discount(discount) - Reduces the price by [discount]% 
"""
""" 
class book:
    def __init__(self,tittle,author,price):
        self.tittle=tittle
        self.author=author
        self.price=price
    def get_info(self):

        return f"Title: {self.tittle}, Author:{self.author}, Price: {self.price}"
    def apply_discount(self,discount):
        self.price = self.price * (1 - discount / 100)

obj=book("The fly","william",200)
print(obj.get_info())
obj.apply_discount(10)
print(obj.get_info()) 
"""
#output
#Title: The fly, Author:william, Price: 200
#Title: The fly, Author:william, Price: 180.0

#Exercise 4: Bank Account

""" 
Create a class BankAccount with:

Attributes: account_holder, balance (default 0)
Methods:
deposit(amount) - Increases balance by amount
withdraw(amount) - Decreases balance by amount if funds are sufficient
get_balance() - Returns the current balance 
"""
""" 
class bankaccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print (f"Insufficient  funds...your balance ${self.balance}")   
            
    def get_balance(self):
        return f"Your balance: ${self.balance }"    
account = bankaccount("Agash", 100)
account.deposit(50)     
account.withdraw(30)     
print(account.get_balance())    
"""

#Output:
#Deposited $50. New balance: $150
#Withdrew $30. New balance: $120
#Your balance: $120

#Exercise 5: Rectangle Class

"""
 Create a class Rectangle with:

Attributes: length, width
Methods:
area() - Returns the area of the rectangle
perimeter() - Returns the perimeter of the rectangle
"""
""" 
class Rectangular:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return f"area of rectangle { self.length * self.width}" 
    def perimeter (self):
        return f"perimeter of rectangle { self.length + self.width}"    
obj=Rectangular(20,30)
print(obj.area())
print(obj.perimeter()) 
"""

#outpur:
#area of rectangle 600
#perimeter of rectangle 50
