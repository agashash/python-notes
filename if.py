"""  1. Assign 8 to the variable x and 15 to the variable y.

In the same cell, create 2 conditional statements.

Let the first one print "At least one of the conditions is satisfied." if x is greater than 3 or y is even.

Let the second one print "Neither condition is satisfied." if x is less than or equal to 3 and y is odd.

Change the values assigned to x and y and re-run the cell to verify your code still works. """
"""
x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
if (x>3) or (y%2==0):
    print("At least one of the conditions is satisfied.")
elif (x<=3) and (y%2!=0):
    print("Neither condition is satisfied.")
else:
    print("no condition satisfied!") """


"""  2. Write a program that takes two numbers as input from the user and prints which number is larger. If they are equal, print a message stating that they are equal. """

""" 
x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
if(x>y):
    print("x is greater")
elif (y>x):
    print("y is greater")
else:
    print("both are equal!")   """      

""" 
3. Create a program that asks the user to enter a number and determines whether the number is odd or even. Print the result accordingly. """
""" 
x=int(input("enter a number:"))
if(x%2==0):
    print("even")
else:
    print("odd") """    

""" 4. Write a program that takes a score (0-100) from the user and prints the corresponding grade:

A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: below 60 """
""" 
x=int(input("enter a number:"))
if x>=90:
    print("grade:A")
elif x>=80:
    print("grade:B")
elif x>=70:
    print("grade:C")
elif x>=60:
    print("grade:D")
else :
    print("grade:F")             """


""" 5. Age Group
Ask the user to input their age and print the following based on the input:

"Child" if age is less than 13
"Teenager" if age is between 13 and 19
"Adult" if age is 20 or older """

""" 
age=int(input("Enter your age:"))
if age<=13:
    print("child")
elif age>13 and age<=19:
    print("teenager")
elif age>=20:
    print("Adult")
else:
    print("invalid input!")            
 """

""" 6.Password Checker
Write a program that prompts the user for a password. If the password is "python123", print "Access granted". Otherwise, print "Access denied". """
""" 
x=input("Enter a password:")
if x=="python123":
    print("Access granted")
else:
    print("invalid password!")     """

""" 7.Define a username and password.
Get the username and password from the user using input().
Use an if statement to check if both match.
Print "Login successful" if they match, otherwise print "Login failed". """
""" 
UserId=input("Enter user Id:")
password=input("Enter your password:")
if UserId=="A1233" and password=="123":
    print("login sucessful")
else:
    print("invalid userid or password")    

    """
""" 
8. Write a program that takes two numbers from the user and compares them.

Instructions:

Get two numbers from the user.
Use if, elif, and else to determine:
If the first number is greater, print "First number is greater."
If the second number is greater, print "Second number is greater."
If they are equal, print "Both numbers are equal."
 """
""" 
num1=int(input("Enter a Number:"))
num2=int(input("Enter a Number:"))
if num1>num2:
    print("First Number Greater")
elif num1<num2:
    print("Second Number Greater") 
else:
    print("Both are Equal") """   


""" 

 9.Write a program that checks if a person is eligible to vote based on their age and citizenship status.

Instructions:

Ask the user for their age and whether they are a citizen (yes or no).
Use an if statement to check:
If the age is 18 or older and the user is a citizen, print "You are eligible to vote."
Otherwise, print "You are not eligible to vote." 

 """  
""" 
age=int(input("Enter your age:"))
if age<18:
    print("Not Eligible for Voting")
else:
    print("Eligible for Voting")  
    
"""   