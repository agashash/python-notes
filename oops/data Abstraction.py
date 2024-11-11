#what is data abstration ?
'''
At its heart, data abstraction in Python is about simplifying complex reality by modeling classes appropriate to the problem. It hides the complex reality while exposing only the necessary parts. Think of it as a way to define and manage the attributes and methods of objects in a more user-friendly way. It’s like seeing a car as a whole without worrying about each individual screw and bolt that holds it together.

In Python, you achieve data abstraction primarily through classes and objects. This keeps the details hidden and the user interfaces simple and efficient. 🚗➝🧩🚗

Want to dive deeper into classes and objects, or shall we shift gears to something else?'''

#Example:

'''from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Usage
dog = Dog()
cat = Cat()
print(dog.make_sound())  # Woof!
print(cat.make_sound())  # Meow!'''

#1.Create an abstract class LibraryItem that:

"""Has attributes: title, author, item_id.
Contains the following abstract methods:
check_out(): To check out an item.
return_item(): To return an item.
get_details(): To display the details of the item."""
'''
from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.is_checked_out = False  # Keeps track of whether the item is checked out or not
    
    @abstractmethod
    def check_out(self):
        """To check out an item."""
        pass

    @abstractmethod
    def return_item(self):
        """To return an item."""
        pass

    @abstractmethod
    def get_details(self):
        """To display the details of the item."""
        pass'''

# Now you can create subclasses like Book and Magazine which will inherit from LibraryItem

#2.Create two subclasses of LibraryItem:

#Book:
'''Additional attributes: genre, number_of_pages.
Implements the abstract methods.'''
#Magazine:
'''Additional attributes: issue_number, publication_date.
Implements the abstract methods.'''

# Importing the base class LibraryItem
""" from abc import ABC, abstractmethod

# Abstract class LibraryItem
class LibraryItem(ABC):
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.is_checked_out = False
    
    @abstractmethod
    def check_out(self):
        '''To check out an item.'''
        pass

    @abstractmethod
    def return_item(self):
        '''To return an item.'''
        pass

    @abstractmethod
    def get_details(self):
        '''To display the details of the item.'''
        pass

# Subclass Book
class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre, number_of_pages):
        super().__init__(title, author, item_id)
        self.genre = genre
        self.number_of_pages = number_of_pages

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"The book '{self.title}' has been checked out.")
        else:
            print(f"The book '{self.title}' is already checked out.")

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' was not checked out.")

    def get_details(self):
        return f"Book - Title: {self.title}, Author: {self.author}, ID: {self.item_id}, Genre: {self.genre}, Pages: {self.number_of_pages}, Checked Out: {self.is_checked_out}"

# Subclass Magazine
class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number, publication_date):
        super().__init__(title, author, item_id)
        self.issue_number = issue_number
        self.publication_date = publication_date

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"The magazine '{self.title}' has been checked out.")
        else:
            print(f"The magazine '{self.title}' is already checked out.")

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"The magazine '{self.title}' has been returned.")
        else:
            print(f"The magazine '{self.title}' was not checked out.")

    def get_details(self):
        return f"Magazine - Title: {self.title}, Author: {self.author}, ID: {self.item_id}, Issue: {self.issue_number}, Publication Date: {self.publication_date}, Checked Out: {self.is_checked_out}"

# Example usage
if __name__ == "__main__":
    # Creating a book instance
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 101, "Fiction", 180)
    book.check_out()  # Checking out the book
    print(book.get_details())  # Getting details of the book
    book.return_item()  # Returning the book

    # Creating a magazine instance
    magazine = Magazine("National Geographic", "Various", 202, 120, "2023-10-01")
    magazine.check_out()  # Checking out the magazine
    print(magazine.get_details())  # Getting details of the magazine
    magazine.return_item()  # Returning the magazine
 """
 
 #3.For both subclasses, ensure that:
 
''' The check_out() method marks the item as checked out and prevents further checkout until it's returned.
 The return_item() method makes the item available for checkout again.
 The get_details() method displays all relevant information about the item (e.g., title, author, etc.).
 '''


'''from abc import ABC, abstractmethod

# Abstract class LibraryItem
class LibraryItem(ABC):
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.is_checked_out = False  # To track checkout status

    @abstractmethod
    def check_out(self):
        """Marks the item as checked out."""
        pass

    @abstractmethod
    def return_item(self):
        """Marks the item as returned (available for checkout)."""
        pass

    @abstractmethod
    def get_details(self):
        """Displays the item's details."""
        pass

# Subclass Book
class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre, number_of_pages):
        super().__init__(title, author, item_id)
        self.genre = genre
        self.number_of_pages = number_of_pages

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"The book '{self.title}' has been successfully checked out.")
        else:
            print(f"Sorry, the book '{self.title}' is already checked out.")

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' was not checked out.")

    def get_details(self):
        return (f"Book - Title: {self.title}, Author: {self.author}, ID: {self.item_id}, "
                f"Genre: {self.genre}, Pages: {self.number_of_pages}, Checked Out: {self.is_checked_out}")

# Subclass Magazine
class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number, publication_date):
        super().__init__(title, author, item_id)
        self.issue_number = issue_number
        self.publication_date = publication_date

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"The magazine '{self.title}' has been successfully checked out.")
        else:
            print(f"Sorry, the magazine '{self.title}' is already checked out.")

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"The magazine '{self.title}' has been returned.")
        else:
            print(f"The magazine '{self.title}' was not checked out.")

    def get_details(self):
        return (f"Magazine - Title: {self.title}, Author: {self.author}, ID: {self.item_id}, "
                f"Issue Number: {self.issue_number}, Publication Date: {self.publication_date}, "
                f"Checked Out: {self.is_checked_out}")

# Example usage
if __name__ == "__main__":
    # Creating a book instance
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 101, "Fiction", 180)
    
    # Checking out the book
    book.check_out()  # Should mark the book as checked out
    print(book.get_details())  # Should print book details
    book.check_out()  # Trying to check out again, should prevent this
    
    # Returning the book
    book.return_item()  # Should return the book
    book.return_item()  # Trying to return the book again, should prevent this
    
    # Creating a magazine instance
    magazine = Magazine("National Geographic", "Various", 202, 120, "2023-10-01")
    
    # Checking out the magazine
    magazine.check_out()  # Should mark the magazine as checked out
    print(magazine.get_details())  # Should print magazine details
    magazine.check_out()  # Trying to check out again, should prevent this
    
    # Returning the magazine
    magazine.return_item()  # Should return the magazine
    magazine.return_item()  # Trying to return the magazine again, should prevent this'''

#output:

'''The book 'The Great Gatsby' has been successfully checked out.
Book - Title: The Great Gatsby, Author: F. Scott Fitzgerald, ID: 101, Genre: Fiction, Pages: 180, Checked Out: True
Sorry, the book 'The Great Gatsby' is already checked out.
The book 'The Great Gatsby' has been returned.
The book 'The Great Gatsby' was not checked out.
The magazine 'National Geographic' has been successfully checked out.
Magazine - Title: National Geographic, Author: Various, ID: 202, Issue Number: 120, Publication Date: 2023-10-01, Checked Out: True
Sorry, the magazine 'National Geographic' is already checked out.
The magazine 'National Geographic' has been returned.
The magazine 'National Geographic' was not checked out.
'''