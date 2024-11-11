""" 
Exercise 1: Counting Down
Question: Count down from 10 to 1.

Expected Output:
10
9
8
7
6
5
4
3
2
1 
"""
""" 
x=10
while(x>0):
    print(x)
    x-=1 
"""

""" 
Exercise 2: Sum of Natural Numbers
Question: Calculate the sum of natural numbers up to a given number n.

Expected Output (for n = 5):

The sum of natural numbers up to 5 is: 15 
"""
""" 
n=int(input("Enter a Number:"))
sum=0
count=1
while count<=n:
    sum=count+sum
    count=count+1
print(f"The sum of {n} is {sum}")  
"""  
""" 
Exercise 3: User Input Validation
Question: Ask the user to enter a number between 1 and 10 until they provide valid input.

Expected Output (if user enters 0, then 5):

Enter a number between 1 and 10: 0
Enter a number between 1 and 10: 5
Thank you! You entered: 5
 """
"""
number = 0

while number < 1 or number > 10:
    number = int(input("Enter a number between 1 and 10: "))

print("Thank you! You entered:", number)
 """

""" 
Exercise 4: Fibonacci Sequence
Question: Print the Fibonacci sequence up to n terms, where n is provided by the user.

Expected Output (for n = 5):

0 1 1 2 3 
"""
""" 
n = int(input("Enter the number of terms in the Fibonacci sequence: "))
a, b = 0, 1
count = 0

while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
 """
""" 
5.Exercise:Game using Random  numbers
import random

num_guess = random.randint(1, 20)
guess = 0

while guess != num_guess:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess < num_guess:
        print("Too low! Try again.")
    elif guess > num_guess:
        print("Too high! Try again.")

print("Congratulations! You've guessed the number:", num_guess)
 """