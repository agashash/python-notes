#polymorphism
""" 
       Polymorphism in Python refers to the ability of different objects to respond to the same method or operation in a way that is specific to their class. In simpler terms, it allows a function or method to process objects of different types in the same way while letting each object exhibit behavior specific to its own class.
"""
#Key Concept of Polymorphism:

""" The concept is based on the principle of "one interface, many implementations." This means that different classes can define methods with the same name, but with distinct behaviors that depend on the class's characteristics."""

#Types of Polymorphism in Python:

#Duck Typing (Informal Polymorphism)
#oprrator overloading
#Method Overriding (Formal Polymorphism)
#Method Overloading (Though Python doesn't support it directly)

#Exersises

""" 
1. Animal Sounds:
Create a base class Animal with a method speak(). Then, create subclasses Dog, Cat, and Cow, each overriding speak() with its respective sound. Write a function that takes a list of Animal objects and calls speak() for each. 
"""
""" 
# Base class
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Subclass Dog
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Subclass Cat
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Subclass Cow
class Cow(Animal):
    def speak(self):
        return "Moo!"

# Function to iterate over a list of animals and call their speak method
def animal_sounds(animals):
    for animal in animals:
        print(animal.speak())

# Create a list of animals
animals = [Dog(), Cat(), Cow()]

# Call the function to make each animal speak
animal_sounds(animals) """

#output:
# Woof!
#Meow!
#Moo!


#2. Shape Area:
"Create a base class Shape with a method area(). Subclasses like Circle, Rectangle, and Triangle should override area() to return the correct value for each shape. Test it by creating objects and calculating areas."
""" 
import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Subclass Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

# Subclass Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Subclass Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Test the implementation by creating objects and calculating areas
def print_area(shape):
    print(f"The area is: {shape.area()}")

# Create instances of each shape
circle = Circle(5)  # Circle with radius 5
rectangle = Rectangle(4, 6)  # Rectangle with width 4 and height 6
triangle = Triangle(3, 4)  # Triangle with base 3 and height 4

# Print the area of each shape
print_area(circle)    
print_area(rectangle) 
print_area(triangle)    
"""

#output:
#The area is: 78.53981633974483
#The area is: 24
#The area is: 6.0

#3. Payment System:
"Create a base class PaymentMethod with a method pay(amount). Implement subclasses like CreditCard, PayPal, and BankTransfer with their unique pay() implementations. Simulate a payment process with different methods."

# Base class
""" 
class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("Subclass must implement abstract method")

# Subclass CreditCard
class CreditCard(PaymentMethod):
    def __init__(self, card_number, cardholder_name):
        self.card_number = card_number
        self.cardholder_name = cardholder_name

    def pay(self, amount):
        print(f"Processing credit card payment of ${amount:.2f} for {self.cardholder_name}...")
        # Simulate a successful payment
        print(f"Payment of ${amount:.2f} completed using Credit Card ending in {self.card_number[-4:]}.\n")

# Subclass PayPal
class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Processing PayPal payment of ${amount:.2f} for {self.email}...")
        # Simulate a successful payment
        print(f"Payment of ${amount:.2f} completed using PayPal account: {self.email}.\n")

# Subclass BankTransfer
class BankTransfer(PaymentMethod):
    def __init__(self, bank_account_number):
        self.bank_account_number = bank_account_number

    def pay(self, amount):
        print(f"Processing bank transfer of ${amount:.2f} from account {self.bank_account_number}...")
        # Simulate a successful payment
        print(f"Payment of ${amount:.2f} completed via Bank Transfer from account: {self.bank_account_number}.\n")

# Simulate a payment process
def process_payment(payment_method, amount):
    payment_method.pay(amount)

# Create instances of each payment method
credit_card = CreditCard("1234567812345678", "John Doe")
paypal = PayPal("john.doe@example.com")
bank_transfer = BankTransfer("9876543210")

# Simulate payments with different methods
process_payment(credit_card, 150.00)      
process_payment(paypal, 75.50)           
process_payment(bank_transfer, 200.25)   
"""

#output:

#Processing credit card payment of $150.00 for John Doe...
#Payment of $150.00 completed using Credit Card ending in 5678.

#Processing PayPal payment of $75.50 for john.doe@example.com...
#Payment of $75.50 completed using PayPal account: john.doe@example.com.

#Processing bank transfer of $200.25 from account 9876543210...
#Payment of $200.25 completed via Bank Transfer from account: 9876543210.


#4. Media Player:
'Create a base class MediaPlayer with a method play(). Subclasses MP3Player, MP4Player, and WAVPlayer should implement play() for different file types. Test it with different player objects.'

""" 
# Base class
class MediaPlayer:
    def play(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Subclass MP3Player
class MP3Player(MediaPlayer):
    def __init__(self, filename):
        self.filename = filename
    
    def play(self):
        print(f"Playing MP3 file: {self.filename}...")

# Subclass MP4Player
class MP4Player(MediaPlayer):
    def __init__(self, filename):
        self.filename = filename
    
    def play(self):
        print(f"Playing MP4 video: {self.filename}...")

# Subclass WAVPlayer
class WAVPlayer(MediaPlayer):
    def __init__(self, filename):
        self.filename = filename
    
    def play(self):
        print(f"Playing WAV file: {self.filename}...")

# Function to simulate playing media files
def play_media(player):
    player.play()

# Test the implementation
mp3_player = MP3Player("song.mp3")
mp4_player = MP4Player("video.mp4")
wav_player = WAVPlayer("sound.wav")

# Play the media files using different players
play_media(mp3_player) 
play_media(mp4_player) 
play_media(wav_player) 
"""  

#output:
# Playing MP3 file: song.mp3...
#Playing MP4 video: video.mp4...
#Playing WAV file: sound.wav...

#Exercise:5 Create a Vector class that supports basic operator overloading.
"Define a Vector class to represent a 2D vector with x and y coordinates. Implement operator overloading so you can:"
""" 
Add two vectors using +.
Subtract two vectors using -.
Multiply a vector by a scalar (number) using *.
Compare two vectors using equality ==.
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload the + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overload the - operator
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # Overload the * operator (for scalar multiplication)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # Overload the == operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Helper method for printing the vector
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Testing the overloaded operators
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Vector addition
v3 = v1 + v2
print(v3)  # Output: Vector(6, 8)

# Vector subtraction
v4 = v1 - v2
print(v4)  # Output: Vector(-2, -2)

# Scalar multiplication
v5 = v1 * 3
print(v5)  # Output: Vector(6, 9)

# Equality comparison
v6 = Vector(2, 3)
print(v1 == v6)  # Output: True



              