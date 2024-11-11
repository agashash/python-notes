""" 
1.Exercise Questions
Sum of Digits: Write a function sum_of_digits(n) that takes a non-negative integer n and returns the sum of its digits.

# Example
print(sum_of_digits(123))  # Output: 6 
"""
""" 
def sum_of_digits(a,b,c):
    return(a+b+c)
print(sum_of_digits(1,2,3)) 
"""
""" 
2.Check Prime: Write a function is_prime(num) that checks if a given number num is a prime number. The function should return True if it is prime and False otherwise.
# Example
print(is_prime(7))   # Output: True
print(is_prime(10))  # Output: False 
"""
""" 
def is_prime(num):
    if num <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Found a divisor, not a prime
    return True  # No divisors found, it is prime
print(is_prime(6))
 """

""" 
3.Fibonacci Sequence: Write a function fibonacci(n) that returns the first n numbers in the Fibonacci sequence as a list.

# Example
print(fibonacci(5))  # Output: [0, 1, 1, 2, 3] 
"""
""" 
def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [1,2]
    fibo_op=[1,0]
    for i in range(2,n):
        num=fibo_op[-1]+fibo_op[-2]
        fibo_op.append(num)
    return fibo_op    
print(fibonacci(7)) """

""" 
4.Count Vowels: Write a function count_vowels(s) that counts the number of vowels (a, e, i, o, u) in a given string s.
# Example
print(Count Vowels: Write a function count_vowels(s) that counts the number of vowels (a, e, i, o, u) in a given string s.

python
Copy code
# Example
print(count_vowels("hello world"))  # Output: 3)  # Output: 3 
"""

""" 
def count_vowels(n):
    vowels='aeiouAEIOU'
    count=0

    for i in n:
        if i in vowels:
            count=count+1
    return count

print(count_vowels("a")) """

"""
5.Palindrome Check: Write a function is_palindrome(s) that checks if the given string s is a palindrome (reads the same forwards and backwards).

# Example
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))   # Output: False 
"""
""" 
def is_palindrome(n):
    n=n.replace(" ","").lower()
    if n==n[::-1]:
        return True
    else:
        return False
print(is_palindrome("Malay  alam"))     
"""
"""
6.Find Maximum: Write a function find_max(lst) that takes a list of numbers and returns the maximum number from the list. If the list is empty, return None.

# Example
print(find_max([1, 2, 3, 4, 5]))  # Output: 5
print(find_max([])) 
"""
""" 
def find_max(n):
    if not n:  # Check if the list is empty
        return None
    
    max_value = n[0]  # Initialize max_value with the first element
    
    # Iterate through the list to find the maximum
    for i in n:
        if i > max_value:
            max_value = i
            
    return max_value
print(find_max([1, 2, 3, 4, 5]))
 """