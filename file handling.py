#1. What are the different modes for opening a file in Python?
   
""" 
In Python, you can open files in various modes:

'r': Read (default mode).
'w': Write (creates a new file or truncates an existing file).
'a': Append (adds to an existing file).
'b': Binary mode.
'x': Exclusive creation (fails if the file already exists). 
"""
""" 
file=open('file_name.txt','x')
file.write("hi,how are u?")
file.close() 
"""

#2.How do you read the entire content of a file into a string?

"""
file=open('file_name.txt','r')
a=file.read()
print(a) 
"""

#3.How can you read a file line by line?

""" 
file=open('file_name.txt','r')
read=file.readlines()
print(read[0:2]) 
"""

#4.What is the difference between read(), readline(), and readlines()?

'read(): Reads the entire file at once.'
'readline(): Reads the next line from the file.'
'readlines(): Reads all lines into a list.'

#5.How do you write to a file in Python?
"""
 file=open("file_name.txt",'w')
file.write("Hi, How are you?")
file.close() 
"""

#6.What is the purpose of using a with statement when handling files?

' The with statement ensures proper acquisition and release of resources. It automatically closes the file after the block is executed, even if an error occurs.'

#7. How does using with open(...) as ...: improve file handling?

"""
 with open('file_name.txt', 'r') as file:
    content = file.read()
    print (content)
"""
#8. How can you check if a file exists in Python?

""" 
import os

if os.path.exists('file_name.txt'):
    print("File exists.")
else:
    print("File does not exist.") 
"""

#9. What methods can you use to get file size and other attributes?

""" 
import os

file_info = os.stat('Exception Handling.py')
print(f"File size: {file_info.st_size} bytes") 
"""

#10. How do you rename or delete a file in Python?

# Renaming a file
"os.rename('output.txt', 'new_output.txt')"

""" 
import os
os.rename( 'new_output.txt','file_name.txt')
"""

# Deleting a file
"os.remove('new_output.txt')"
""" 
import os
os.remove('file_name.txt') 
"""

#11. What exceptions might you encounter while working with files, and how can you handle them?

""" 
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.") 
"""

#12. How would you handle an IOError when trying to open a file?
  
""" 
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except IOError:
    print("IoError occurs")
"""
#13. How can you read and write CSV files in Python?

#import csv

# Writing to a CSV file
"""
 with open('data.csv','w',newline="") as file:
    content=csv.writer(file)
    content.writerow(['alice','23'])
    content.writerow(['agash','21']) 
"""

 # Reading from a CSV file
""" 
with open('data.csv','r') as file:
    content=csv.reader(file)
    for i in content:
        print(i) 
"""
#14. What libraries can be used to handle JSON files in Python?

import json
"""
# Writing to a JSON file
data = {'name': 'Alice', 'age': 30}
with open('data.json','w') as file:
    json.dump(data,file)
""" 
# Reading from a JSON file
"""
with open('data.json','r') as file:
    content=json.load(file)
    print(content)
"""
#15. How do you work with binary files, and what are some common use cases?

# Writing binary data
""" 
data = bytes([0, 1, 2, 3, 4, 5])
with open('binary.dat', 'wb') as file:
    file.write(data) 
"""

# Reading binary data
""" 
with open('binary.dat','rb') as file:
    content=file.read()
    print(content) 
"""

#16. What is the difference between text and binary mode when opening a file?

"""
#Text mode ('t'): Reads/writes strings.
#Binary mode ('b'): Reads/writes bytes
"""

#17. How can you efficiently handle large files that don’t fit into memory?

""" 
def process(line):
    print(line.strip())  # Print each line without leading/trailing whitespace

with open('large_file.txt', 'r') as file:
    for line in file:
        process(line)
"""

#18. What are file iterators, and how do they work in Python?

'File objects in Python are iterators, which means you can use them directly in a for loop to iterate over lines.'

#19. How can you append data to an existing file?

with open('file_name.txt','a') as file:
   file.write("\nagash,Epadi iruka ") #\n used to add in next line
   
