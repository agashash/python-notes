
#syntax: Lambda function
""" 
fn_name = keyword parameter : expression
"""
"sample : Example."#lambda function
"""
lam_fun=lambda a,b:a**b
print(lam_fun(2,3))
"""
#Question 1: Map function
""" 

Create a lambda function that takes a list of integers and returns a list of their squares.

Expected Output:
[1, 4, 9, 16, 25] 
"""
#sytax for map fun: 
     #map(function, iterable)

""" 
num=[1,2,3,4,5,6]
fun_name=lambda a:a**2
c=map(fun_name,num)
print(tuple(c))
 """
#Question 2: sorted function
""" 
Write a lambda function to sort a list of tuples based on the second element in each tuple.

Expected Output

[(3, 1), (2, 2), (1, 3)] 
"""
"""
 num=[(1,3),(2,2),(3,1)]
result=sorted(num,key=lambda a:a[0])
print(list(result)) 
"""

# Question 3: Filter function
"""
Create a lambda function that checks if a string starts with a vowel.

Expected Output

['apple', 'orange'] 
"""
"""
 words = ["Apple", "banana", "orange", "grape"]
fun_name=list(filter(lambda a:a[0].upper() in 'AEIOU',words)) #while using lower "aeiou"
print(fun_name) 
"""
#Question 4 :Lambda function
""" 
Implement a lambda function that concatenates two strings.

Expected Output

Hello, World!
"""
""" 
num=lambda a,b:a+b
num1=num("hello", "world")

print(num1) 
"""

#Question 5: Reduce function
"""
Create a lambda function to find the maximum number in a list.

Expected Output:
30 
"""
""" 
from functools import reduce
numbers = [10, 20, 5, 30, 15]
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)
"""
            #or
""" 
import functools
num=[1,9,70,111,1,8]
c=functools.reduce(lambda x,y: x if x>y else y,num)
print(c) """


#6.Question:Zip function()
""" 
You have two lists: one with student names and another with their corresponding grades. Combine these lists into a list of tuples using the zip() function and print the result.
 """
""" 
students = ["Alice", "Bob", "Charlie"]
grades = [85, 90, 78]
print(list(zip(students,grades)))
"""
#output:[('Alice', 85), ('Bob', 90), ('Charlie', 78)]

#7.Question:Enumuration Function
""" 
You have a list of fruits. Use the enumerate() function to create a list of tuples, where each tuple contains the index and the corresponding fruit. Print the resulting list """

""" 
fruits = ["apple", "banana", "cherry", "date"]
c=(enumerate(fruits)) # It is used to add key value in frond start=0
print (list(c)) 
"""

#output: [(0, 'apple'), (1, 'banana'), (2, 'cherry'), (3, 'date')]

#8.Question: list comprehension : use[]
""" 
You have a list of numbers. Use list comprehension to create a new list that contains the squares of all even numbers from the original list. Print the resulting list. 
"""

'a=[x**2 for x in range(1,11) if x%2==0 ] '# if u want to use else part you must use if in fist after the expression,    
'print(a)'                                 # otherwise use the if in  last

#output:[4, 16, 36, 64, 100]

#9.Question: Generator comprehension: use()
'You have a list of integers. Use generator comprehension to create a generator that yields the cubes of all odd numbers from the original list. Print the cubes by iterating through the generator.'

'a=(x**3 for x in range(1,11) if x%2==0)'# if u want to use else part you must use if in fist after the expression,   
'print(tuple(a))'                        # otherwise use the if in  last, In this we wnt to mension the brackets(list,set,tuples)

#output:(8, 64, 216, 512, 1000)
