""" 
1. Multiplication Table
Write a program that prints a multiplication table from 1 to 10.

Example Output:

python
Copy code
1  2  3  4  5  6  7  8  9  10
2  4  6  8  10 12 14 16 18 20
3  6  9  12 15 18 21 24 27 30 

"""
""" 
n=11

for i in range (1,n):
    for j in range(1,n):
        print(i*j,end=" ")
    print()
 """

""" 
2.Floyd's Triangle
Write a program to print Floyd's triangle, which is a right-angled triangular array of natural numbers.

Example Output (for 5 rows):

Copy code
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15 """


""" 
n = 5
current_number = 1
for i in range(1, n+1):
    for j in range(i):
        print(current_number, end=' ')
        current_number += 1 
    print() 
 """

""" 
3. Cartesian Product
Question: Print the Cartesian product of two lists.

Output Example:


(1, A)
(1, B)
(1, C)
(2, A)
(2, B)
(2, C)
(3, A)
(3, B)
(3, C) 

"""
""" 
x=3
for i in range ( 1,x+1):
    for j in  ['a','b','c']:
        print(f"({i},{j})")    
        
"""   
      
""" 
4.Nested List Creation
Question: Create a 3x3 matrix filled with the product of row and column indices.

Output:

[0, 0, 0]
[0, 1, 2]
[0, 2, 4]

"""
""" 
matrix=[]
for i in range(3):
    row=[]
    for j in range(3):
        row.append(i * j)
    matrix.append(row)
for k in matrix:
    print(k)      
 """
""" 
5.Spiral Matrix
Question: Generate a spiral matrix of size n x n filled with numbers from 1 to n^2.

Output for n = 3:

1 2 3
8 9 4
7 6 5
Feel free to ask if you need more details or clarifications!
"""
????????