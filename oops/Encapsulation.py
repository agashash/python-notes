#public method

#Exercise: Bank Account Class
'Create a class BankAccount with the following:'

#Attributes:
""" 
account_number (public)
balance (public)
"""
#Methods: 
""" 
deposit(amount): Adds amount to the account balance.
withdraw(amount): Subtracts amount from the balance if there are sufficient funds.
display_balance(): Displays the current balance.

"""
""" 
class BankAccount:
    def __init__(self,acc_no,balance=0):
        self.acc_no=acc_no
        self.balance=balance
        print(f"Your Account Number is {self.acc_no}")
        

    def deposit(self,amount):
        self.amount=amount
        self.balance += self.amount
        print (f"your balance is {self.balance} ")

    
    def withdraw(self,amount):
        self.amount=amount
        if self.amount<=self.balance:
            self.balance -= self.amount
            print(f"Your withdraw Amount is {self.amount}")
            print (f"your balance is {self.balance} ")
        else:
            print(f"Insuficcient balance")

    def check_bal(self):
        print(f"your balace is {self.balance}")


# Create an account with account number 12345 and balance 1000
account = BankAccount(12345, 1000)  
# Output: Your Account Number is 12345

# Deposit 500
account.deposit(500)        
# Output: your balance is 1500

# Withdraw 300
account.withdraw(300)       
# Output: Your withdraw Amount is 300
#         your balance is 1200

# Withdraw 2000 (which exceeds the balance)
account.withdraw(2000)      
# Output: Insufficient balance

# Check balance
account.check_bal()         
# Output: your balance is 1200
"""

#private method:

#Exercise: Authentication System
'''
Create a class called Authentication that simulates a user login system with both public and private methods.
'''
#Attributes:
'''username (public)
password (private)'''

#Methods:
""" 
login(username, password): This is a public method that allows the user to log in. It checks if the username matches and calls a private method to verify the password.
_verify_password(password): This is a private method that checks if the provided password matches the stored password. """

""" 
class Authentication:
    def __init__(self, username, password):
        self.username = username          # Public attribute
        self.__password = password        # Private attribute

    def login(self, username, password):
        if username == self.username and self._verify_password(password):
            print("Login successful!")
        else:
            print("Login failed!")

    def change_password(self, old_password, new_password):
        if self._verify_password(old_password):
            self.__password = new_password
            print("Password changed successfully!")
        else:
            print("Old password is incorrect.")

    def _verify_password(self, password):
        return self.__password == password  # Private method for password verification

# Example Usage
# Create a user object with a username and password
user = Authentication("john_doe", "secure123")

# Attempt to log in with the correct username and password
user.login("john_doe", "secure123")   # Output: Login successful!

# Attempt to change the password
user.change_password("secure123", "newpassword123")  # Output: Password changed successfully!

# Attempt to log in with the new password
user.login("john_doe", "newpassword123")  # Output: Login successful!

# Attempt to change the password with an incorrect old password
user.change_password("wrongoldpass", "anotherpassword")  # Output: Old password is incorrect. 
"""


#protected method

""" 
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make          # Public attribute
        self.model = model        # Public attribute
        self.year = year          # Public attribute

    def _display_info(self):      # Protected method
        print(f"Vehicle Info: {self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)  # Initialize base class attributes
        self.num_doors = num_doors            # Public attribute

    def display_car_info(self):
        self._display_info()                  # Call the protected method from the base class
        print(f"Number of doors: {self.num_doors}")

# Example Usage
# Create a Car object
my_car = Car("Toyota", "Camry", 2022, 4)

# Display car information
my_car.display_car_info()
"""
#output
#Vehicle Info: 2022 Toyota Camry
#Number of doors: 4
