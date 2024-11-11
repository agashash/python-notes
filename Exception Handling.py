                                         #Exeception handling

#1. What happens when you divide by zero?

"""
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
"""
#Output:Cannot divide by zero!

#2. What is the output when a file is not found?

""" 
try:
    file = open('nonexistent_file.txt', 'r')
except FileNotFoundError:
    print("File not found.")
 """
#output:File not found.

#3. What do you see when an invalid input is provided?
""" 
try:
    result = int("abc")
except ValueError:
    print("Invalid input.") 
"""

#output:Invalid input.

#4. What is the output if both exceptions are caught?

""" 
try:
    result = int("abc") / 0
except (ZeroDivisionError, ValueError) as e:
    print("An error occurred:", e) 
"""

#output: An error occurred: invalid literal for int() with base 10: 'abc'

#5. What does the finally block do?

""" 
try:
    print("Trying...")
finally:
    print("This runs no matter what.")
"""
#output:
# Trying...
#This runs no matter what.

#6. What happens when a custom exception is raised?

""" 
class MyError(Exception):
    pass

try:
    raise MyError("Custom error occurred!")
except MyError as e:
    print(e) 
"""

#output: Custom error occurred!

    
#7.What is the output of a traceback print?
""" 
import traceback

try:
    x = 1 / 0
except Exception:
    traceback.print_exc() 
"""

#output: 
#Traceback (most recent call last):
  #File "script.py", line 3, in <module>
    #x = 1 / 0
#ZeroDivisionError: division by zero

#8. What happens if you suppress an exception?

""" 
try:
    x = 1 / 0
except:
    pass
print("Continuing...")
"""

#output: Continuing...


                                                  #Exersises


#Question:1
'You are writing a function that takes two numbers as input and returns their division. Implement exception handling to catch any potential errors, such as division by zero and invalid input types. If an error occurs, return a custom error message.'

""" 
Example Input/Output:
Input: safe_divide(10, 2)
Output: 5.0

Input: safe_divide(10, 0)
Output: "Error: Division by zero is not allowed."

Input: safe_divide(10, 'a')
Output: "Error: Invalid input type. Please provide numbers."

 """
""" 
def safe_divide(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."  """
  
'print(safe_divide(10, 2))'   # Output: 5.0
'print(safe_divide(10, 0)) ' # Output: "Error: Division by zero is not allowed."
"print(safe_divide(10, 'a'))" # Output: "Error: Invalid input type. Please provide numbers." 


#Exercise 2:File Reading
'Create a program that attempts to read a file. If the file does not exist, handle the FileNotFoundError and inform the user. If the file is found, print its contents.'
""" 
try:
    file=open('flowers','r')
    print(file)
    file.close()
   
except (ValueError,FileNotFoundError):
    print('File not found') 
"""

#output: File not found
    

#Exercise 3: Custom Exception
'Define a custom exception called NegativeNumberError. Write a function that takes a number as input and raises this exception if the number is negative. Test this function with user input.'

"""
class NegativeNumberError(Exception):
    pass
def error(num):
    if num<0:
        raise NegativeNumberError
try:
    num=float(int(input("Enter a Positive Number:")))
    error(num)
except NegativeNumberError :
    print("Enter a Positive Number")    
except ValueError :
    print("Error: Enter a valid number")
    
finally:
    print("program executed")    
"""
#output:
#Enter a Positive Number:9
#program executed    
#Enter a Positive Number:-9
#Enter a Positive Number
#program executed    
#Enter a Positive Number:a
#Error: Enter a valid number
#program executed

#Exercise 4: Multiple Exceptions
'Write a program that prompts the user to enter a number and converts it to an integer. Handle both ValueError (for invalid input) and ZeroDivisionError (if the number is zero) when attempting to divide 100 by the input number.also add a error for Negative numbers'
""" 
class NegativeNumberError(Exception):
    pass
def division(num):
    if num==0:
        raise ZeroDivisionError
    elif num<0:
        raise NegativeNumberError
try:
    num=int(input("Enter a number:"))
    result=100/num    
    division(num    )
except ZeroDivisionError:   
    print("error: can't able to divided by zero")
except NegativeNumberError:
    print("Enter a positive Number:")
        
except ValueError:
    print("Invalid input")
else:
    print("The Result is:",result)    
 """
#output:
#Enter a number:10
#The Result is: 10.0
#Enter a number:0
#error: can't able to divided by zero
#Enter a number:-1
#Enter a positive Number:
#Enter a number:a
#Invalid input

#Exercise 5: Finally Block for Cleanup
'Create a program that opens a database connection (simulated with a simple print statement) and ensures that the connection is closed in a finally block, regardless of whether an error occurred during database operations.'

try:
    print("Opening database connection...")
    raise Exception("An error occurred during database operations.")
except Exception as e:
    print("Error:", e)
finally:
    print("Closing database connection...")

#output:
# pening database connection...
#Error: An error occurred during database operations.
#Closing database connection...    



