#Inheritance in Python

""" Inheritance is a feature in object-oriented programming that allows a new class (derived or child class) to inherit properties and behaviors (methods and attributes) from an existing class (base or parent class). This promotes code reuse and establishes relationships between different classes. """

#Key Benefits:

""" Code Reusability: Instead of writing code again, we can reuse the functionality of an existing class.
Maintainability: Changes made to the parent class automatically reflect in the child class.
Extensibility: We can add new functionalities to the child class while retaining the properties of the parent class. """

#Types of Inheritance

"""
1.single inheritance
2.multiple inheritance
3.multilevel inheritance
4.hierarchial inheritace
5.hybrid inheritance 
"""
#Exersises

""" 
1. Basic Inheritance
Create a base class Animal with a method speak(). Then, create two derived classes Dog and Cat that override the speak() method.
"""
""" 
class animal:
     def __init__(self,name):
          self.name=name

     def speak():
          pass
     
class dog(animal):
     def speak(self):
          return f"{self.name} says Woof!"
     
     
class cat(animal):
     def speak(self):
          return f"{self.name} says Meow!"    


dog1=dog("tom")
print(dog1.speak())
cat1=cat("rob")
print(cat1.speak()) 
"""

#output:
#tom says Woof!
#rob says Meow!

"""
 2. Calling Parent Class Methods
Create a base class Animal with a method move(). Override move() in the Dog class while keeping the Cat class unchanged. 
"""

""" 
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass
    
    def move(self):
        return f"{self.name} is moving."

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    
    def move(self):
        return f"{self.name} is running!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Rex")
cat = Cat("Whiskers")

print(dog.move())  
print(cat.move())   
"""

#output:
#Rex is running!
#Whiskers is moving.

""" 
3. Multilevel Inheritance
Create a class Vehicle, then derive a class Car, and finally derive a class ElectricCar. Implement appropriate methods in each class. 
"""
""" 
class vehicles:
    def __init__(self,name):
        self.name=name
    def vehicle_name(self):
        return f"The {self.name} vehicle starts."
class car(vehicles):
    def __init__ (self,name,color):
        super().__init__(name)
        self.color=color
    def vehicle_color(self):
        return f" {self.name} is {self.color} in color"
    
class bike(car):
    def __init__ (self,name,color,cost):
        super().__init__(name,color)
        self.cost=cost
    def vehicle_cost(self):
        return f" {self.name} price is {self.cost}"
    

tesla = bike("Tesla", "red", 10000000)
print(tesla.vehicle_name())    
print(tesla.vehicle_color())   
print(tesla.vehicle_cost()) 
"""

    
#output
# The Tesla vehicle starts.
# Tesla is red in color
# #Tesla price is 10000000


""" 
4. Multiple Inheritance
Create two base classes FlyingAnimal and SwimmingAnimal, and a derived class Penguin that inherits from both. 
"""
""" 
class FlyingAnimal:
    def move(self):
        return "Flying in the sky"

class SwimmingAnimal:
    def move(self):
        return "Swimming in the water"

class Penguin( SwimmingAnimal , FlyingAnimal):
    def move(self):
        return f"Penguins cannot fly. {super().move()}"

penguin = Penguin()
print(penguin.move())   """

# Output: 
# Penguins cannot fly. Swimming in the water

""" 
5. Method Overriding
Create a base class Shape and derived classes Circle and Square. Override the area() method to compute the area for each shape. 
"""

""" 
class shape:
    def area(self):
        return 0
class circle(shape):
    def __init__(self,radius) :
        self.radius=radius
    def area (self):
        return (self.radius**2)
        
class square(shape):
    def __init__(self,length) :
        self.length=length
    def area (self):
        return (self.length*2)
Circle = circle(5)
Square = square(4)

print(Circle.area()) 
print(Square.area()) 
"""
#output:
#25
#8

""" 
6. Use of super() in Initialization
Create a base class Employee with basic details like name and age. Then, create a derived class Manager that adds a department field and use super() to initialize the base class. 
"""

""" 
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Manager(Employee):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def info(self):
        return f"Manager {self.name}, Age: {self.age}, Department: {self.department}"

manager = Manager("Alice", 35, "HR")
print(manager.info())
"""
# Output: 
# Manager Alice, Age: 35, Department: HR

""" 
7. Class Attribute Inheritance
Create a class Appliance with a class attribute category and show that derived classes inherit this attribute but can also override it. 
"""

""" 
class Appliance:
    category = "Home Appliance"

class WashingMachine(Appliance):
    pass

class Refrigerator(Appliance):
    category = "Kitchen Appliance"

washer = WashingMachine()
fridge = Refrigerator()

print(washer.category)  
print(fridge.category) """

# Output: 
# Home Appliance     
# Kitchen Appliance
 
