""" 1. Basic Counting
Write a program that prints the numbers from 1 to 10, each on a new line. """

""" for i in range(1,11):
    print(i) """

""" 
2. Sum of a Range
Create a program that calculates the sum of all numbers from 1 to 100 using a for loop. Print the result.
"""
""" 
sum=0
for i in range(101):
    sum=sum+i
print(sum)  

""" 
""" 
3. Multiplication Table
Generate a multiplication table for the number 7 (from 1 to 10). Print each line in the format: 7 x 1 = 7.

 """
""" 
for i in range(1,11):
    print(7, "x" ,i,"=",i*7) 
    
"""
""" 
4. List Iteration
Given the list fruits = ['apple', 'banana', 'cherry'], write a for loop that prints each fruit in the list. 

"""
"""
 fruit= ['apple', 'banana', 'cherry']
for i in fruit:
    print(i)
 
 """
""" 
5. Count Vowels
Write a program that counts the number of vowels in a given string using a for loop. Print the count. 

"""
""" 
string=input("Enter a string:")
vowels="aeiouAEIOU"
count=0
for i in string:
    if i in vowels:
        count=count+1
print(count)  

"""   
""" 
6. FizzBuzz
Implement the FizzBuzz problem: for numbers from 1 to 100, print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both. Otherwise, print the number itself.

"""   
""" 
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz") 
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)    
 
 """
"""
 7. Reverse a String
Write a program that takes a string and prints it in reverse order using a for loop.

"""
"""
string = "Hello, World!"
reversed= ""
for i in range(len(string)):
    reversed += string[i]
print("Reversed string:", reversed)
print(string[i])

""" 
""" 8.Factorial Calculation

Write a for loop that calculates the factorial of a number (e.g., 5) and prints the result.  """


""" 
num=int(input("Enter a Number:"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(f" The factorial of {num} is {factorial}")    
 """

""" 
9.List Comprehension

Create a list of the squares of the numbers from 1 to 10 using a for loop and print the resulting list. 
"""
""" 
list=[]
for i in range(1,11):
    list.append(i**2)
print(list)   
""" 
""" 
10.Sum of Odd Numbers

Use a for loop to calculate the sum of all odd numbers between 1 and 50 and print the result. 
"""
""" 
sum=0
for i in range(1,51,2):
    sum=sum+i
print(sum) 
print
 """
""" 
11.Generate a Sequence

Write a program that generates the first 10 Fibonacci numbers using a for loop and prints them. 

"""
""" 
n=10
list=[0,1]
for i in range(2,n):
   fib = list[i - 1] + list[i - 2]
   list.append(fib)
print(list)  

"""    
""" 
12.Stars Pattern

Create a pattern of stars using a for loop. For example, print the following:

*****
*****
*****
*****
*****
"""
""" 
n=5
for i in range(n):
    for j in range(n):
         print('*',end=" ")
    print() """

""" 
13. Stars Pattern

Create a pattern of stars using a for loop. For example, print the following:

*
**
***
****
*****
 """

""" 
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print() """

""" 
14.Stars Pattern

Create a pattern of stars using a for loop. For example, print the following:

*****
****
***
**
*   
"""
""" 
n=5
for i in range(n):
    for j in range(i,n):
        print(i,end=" ")
    print() 
    
"""