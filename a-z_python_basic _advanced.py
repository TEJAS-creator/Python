# OUTPUT
name = "Tejas"
age = 20
print("Name:", name, "Age:", age)  # Output: Name: Tejas Age: 20


# INPUT
# Taking an integer input
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# Taking a float input
height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters.")

# Taking multiple inputs
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)



# This is a single-line comment
print("Hello, World!")  # This prints a greeting

"""
This is a multi-line comment.
It is often used to document
large sections of code.
"""

x = 5           # An integer
name = "Tejas"  # A string
price = 99.99   # A float

my_variable = 10      # Valid
_hidden_value = 42    # Valid
# 2cool4school = 17     # Invalid (cannot start with a number)

# Dynamic Typing
x = 10        # x is an integer
x = "Hello"   # Now x is a string

a, b, c = 1, 2, 3   # a=1, b=2, c=3
x = y = z = 0       # x=0, y=0, z=0 (all point to the same value)


# Python supports several built-in types:

# Integers (int): Whole numbers, like 5 or -42.
# Floating-point numbers (float): Numbers with decimals, like 3.14 or -0.01.
# Strings (str): Text enclosed in quotes, like "Hello" or 'Python'.
# Booleans (bool): Logical values True or False.
# Lists (list): Ordered collections, like [1, 2, 3].
# Tuples (tuple): Immutable ordered collections, like (1, 2, 3).
# Dictionaries (dict): Key-value pairs, like {"name": "Tejas", "age": 20}.
# Sets (set): Unordered collections of unique elements, like {1, 2, 3}.

name = "Tejas"         # String
age = 20               # Integer
height = 5.9           # Float
is_student = True      # Boolean
subjects = ["Math", "CS"]  # List

count = 0
count += 1  # Increment count by 1
print(count)  # Output: 1

count = 0
count += 1  # Increment count by 1
print(count)  # Output: 1

height = 5.9   # Float
price = 99.99  # Float

z = 3 + 4j     # Complex number where 3 is the real part and 4 is the imaginary part

name = "Tejas"
message = '''This is a
multi-line string.'''

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Modifying the list
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

numbers = range(5)  # Generates numbers 0, 1, 2, 3, 4

# Dictonary
student = {"name": "Tejas", "age": 20, "is_student": True}
print(student["name"])  # Accessing value by key

# Set and frozenset
unique_numbers = {1, 2, 3, 4, 4, 5}  # Output: {1, 2, 3, 4, 5}
frozen = frozenset([1, 2, 3, 3])  # Output: frozenset({1, 2, 3})

# Numeric
x = 42                 # Integer
y = 3.14               # Float
z = 2 + 3j             # Complex number

# String
greeting = "Hello, Tejas!"

# Boolean
is_valid = True

# List
colors = ["red", "green", "blue"]

# Tuple
point = (10, 20)

# Dictionary
person = {"name": "Tejas", "age": 20}

# Set
letters = {"a", "b", "c"}

# NoneType
result = None

# CASTING

# From float
x = int(5.7)      # Output: 5
# From string
y = int("10")     # Output: 10

# From integer
x = float(10)     # Output: 10.0
# From string
y = float("3.14") # Output: 3.14

# From integer
x = float(10)     # Output: 10.0
# From string
y = float("3.14") # Output: 3.14

bool(1)       # Output: True
bool(0)       # Output: False
bool("Hello") # Output: True
bool("")      # Output: False

# From string
x = list("abc")   # Output: ['a', 'b', 'c']
# From tuple
y = list((1, 2, 3)) # Output: [1, 2, 3]

# From list
x = tuple([1, 2, 3])  # Output: (1, 2, 3)
# From string
y = tuple("hello")    # Output: ('h', 'e', 'l', 'l', 'o')

# From list with duplicates
x = set([1, 2, 2, 3]) # Output: {1, 2, 3}
# From string
y = set("hello")      # Output: {'h', 'e', 'l', 'o'}

# From list of pairs
x = dict([("name", "Tejas"), ("age", 20)]) # Output: {'name': 'Tejas', 'age': 20}


# if ... else
#PROGRAMMING CONCEPTS
age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


#PROGRAMMING CONCEPTS
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")


# PROGRAMMING CONCEPTS
age = 25
is_student = True
# Both conditions need to be true
if age < 30 and is_student:
    print("You are a young student.")
else:
    print("Condition not met.")
# Only one condition needs to be true
if age < 18 or is_student:
    print("You are either a minor or a student.")
else:
    print("Neither condition is met.")
# Negate a condition
if not is_student:
    print("You are not a student.")
else:
    print("You are a student.")


# PROGRAMMING CONCEPTS
age = 16
has_permission = True

if age >= 18:
    print("You can enter.")
else:
    if has_permission:
        print("You can enter with permission.")
    else:
        print("Entry denied.")


# PROGRAMMING CONCEPTS
temperature = int(input("Enter the temperature: "))

if temperature > 30:
    print("It's hot outside.")
elif temperature >= 20:
    print("It's a nice day.")
elif temperature >= 10:
    print("It's a bit chilly.")
else:
    print("It's cold.")


# PROGRAMMING CONCEPTS
if age >= 18:
    pass  # Will do nothing


# WHILE LOOPS
count = 1

while count <= 5:                    
    print("Count is:", count)
    count += 1

while True:
    print("This will print forever!")

# PROGRAMMING CONCEPTS
count = 1
while True:
    print("Count is:", count)
    count += 1
    if count > 5:
        break  # Exit the loop when count exceeds 5

# PROGRAMMING CONCEPTS
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip the iteration when count is 3
    print("Count is:", count)

# PROGRAMMING CONCEPTS
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1
else:
    print("Loop completed without break.")


# MINI PROJECT
secret_number = 7
guess = None
while guess != secret_number:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it right.")


# FOR LOOPS
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("Fruit:", fruit)


# PROGRAMMING CONCEPTS
# Simple example with range
for i in range(5):
    print("Iteration:", i)
# Range with start, stop, and step
for i in range(1, 10, 2):
    print(i)

# PROGRAMMING CONCEPTS
for i in range(3):
    print("Number:", i)
else:
    print("Loop completed without break.")
# OUTPUT
# Number: 0
# Number: 1
# Number: 2
# Loop completed without break.

# PROGRAMMING CONCEPTS
word = "Python"
for char in word:
    print(char)
# P
# y
# t
# h
# o
# n


# TABLES
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()
# OUTPUT
# 1 2 3
# 2 4 6
# 3 6 9


# PROGRAMMING CONCEPTS
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")
# OUTPUT
# Alice scored 85
# Bob scored 92
# Charlie scored 78


# FACTORIAL OF A NUMBER
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")


# FUNCTIONS
def function_name(parameters):
    # Code to execute
    return result

def greet():
    print("Hello, welcome to Python!")
    # Calling the function
greet()

def greet(name):
    print(f"Hello, {name}!")
# Calling the function with an argument
greet("Tejas")

def add(a, b):
    return a + b
result = add(5, 3)
print("Result:", result)

# PROGRAMMING CONCEPTS
global_var = "I'm global"
def modify_global():
    global global_var
    global_var = "Modified global"
modify_global()
print(global_var)

# Lambda function to add two numbers
add = lambda x, y: x + y
print(add(5, 3)) # 8

# NESTED FUNCTION
def outer():
    def inner():                      # OUTPUT
        print("Inner function")       # Inner function
    inner()                           # Outer function
    print("Outer function")
outer()

#FACTORIAL USING FUNCTIONS
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))



# MINI PROJECT
# Define functions for each arithmetic operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y

# Display options for the user
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Get user choice
    choice = input("Enter choice (1/2/3/4): ")

    # Ensure the choice is valid
    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please select a valid operation.")
        return

    # Get numbers from the user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    # Perform the selected operation
    if choice == '1':
        print(f"The result is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result is: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"The result is: {divide(num1, num2)}")

# Call the calculator function
calculator()


# ARRAYS 
# Creating a list (array)
fruits = ["apple", "banana", "cherry"]
print(fruits)

print(fruits[0])  # apple
print(fruits[1])  # banana

fruits[1] = "orange"
print(fruits) # ['apple', 'orange', 'cherry']

# Adding elements
fruits.append("kiwi")      # Add to the end
fruits.insert(1, "mango")  # Insert at index 1
print(fruits)

# Removing elements
fruits=['apple', 'mango', 'orange', 'cherry', 'kiwi']
fruits.remove("apple")     # Remove by value
popped_fruit = fruits.pop() # Remove last element and return it
print(fruits, popped_fruit) # ['mango', 'orange', 'cherry']  # kiwi

# USING NUMPY MODULE FOR ARRAYS
import numpy as np

# Creating a NumPy array from a list
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Creating a 2D NumPy array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
# OUTPUT
# [1 2 3 4 5]

# OUTPUT
# [[1 2 3]
#  [4 5 6]]

print(arr[0])          # First element
print(matrix[1, 2])    # Element at row 1, column 2
print(arr[1:4])        # Slicing 
# OUTPUT
# 1
# 6
# [2 3 4]
# IMPORTANT ELEMENTS ARE ALWAYS FROM 0 TO N-1 

# NOTES:-
# Classes: Blueprints for creating objects. Define attributes and methods.
# Objects: Instances of classes that can hold data and perform operations.
# Methods: Functions defined within a class that operate on the class’s instances.
# Inheritance: Allows classes to inherit attributes and methods from other classes.
# Encapsulation: Restricts access to certain components, promoting data integrity.
# Polymorphism: Allows for methods to be defined in multiple classes with the same name but different behaviors.


# CLASS
class ClassName:
    # Class attribute
    class_attribute = value
    # Constructor method
    def __init__(self, parameter1, parameter2):
        # Instance attributes
        self.attribute1 = parameter1
        self.attribute2 = parameter2
    # Method
    def method_name(self):
        # Code for the method



# OBJECT
# Define a class
     class Dog:
    # Class attribute
      species = "Canine"
    # Constructor method
    def __init__(self, name, age):
        self.name = name      # Instance attribute
        self.age = age        # Instance attribute
    # Method to describe the dog
    def description(self):
        return f"{self.name} is {self.age} years old."
    # Method to simulate a bark
    def bark(self):
        return "Woof!"
# Create an object (instance) of the Dog class
my_dog = Dog("Buddy", 3)
# Accessing attributes
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
# Calling methods
print(my_dog.description())  # Output: Buddy is 3 years old.
print(my_dog.bark())         # Output: Woof!



# METHODS
def instance_method(self):
    # Code that uses instance attributes
 @classmethod
 def class_method(cls):
    # Code that uses class attribute
    @staticmethod
    def static_method():
    # Code that does not use instance or class attributes



# INHERITANCE
# Parent class
        class Animal:
          def __init__(self, name):
             self.name = name
    def speak(self):
        return "Some sound"
# Child class
class Cat(Animal):
    def speak(self):
        return "Meow"
# Create an object of the Cat class
my_cat = Cat("Whiskers")
print(my_cat.name)        # Output: Whiskers
print(my_cat.speak())     # Output: Meow



# ENCAPSULATION
class Person:
    def __init__(self, name, age):
        self.name = name      # Public attribute
        self._age = age       # Protected attribute
        self.__password = ""  # Private attribute

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password
# Create an object
person = Person("Alice", 30)
print(person.name)       # Output: Alice
print(person._age)      # Output: 30
# Accessing private attribute raises an error
# print(person.__password)  # AttributeError

# Using methods to access private attribute
person.set_password("secret")
print(person.get_password())  # Output: secret



# POLYMORPHISM
class Bird:
    def speak(self):
        return "Tweet"
class Dog:
    def speak(self):
        return "Woof"
def animal_sound(animal):
    print(animal.speak())
# Create objects
my_bird = Bird()
my_dog = Dog()
animal_sound(my_bird)  # Output: Tweet
animal_sound(my_dog)   # Output: Woof


# LOCAL SCOPE
def my_function():
    x = 10  # Local variable
    print(x)
my_function()
# print(x)  # This will raise a NameError since x is not accessible outside the function


# GLOBAL SCOPE
y = 20  # Global variable
def another_function():
    print(y)  # Accessing the global variable
another_function()  # Output: 20
print(y)            # Output: 20


# ENCLOSING SCOPE
def outer_function():
    z = 30  # Enclosing variable
    def inner_function():
        nonlocal z  # Declare that we are using the enclosing variable
        z += 5
        print(z)
    inner_function()  # Output: 35
    print(z)          # Output: 35
outer_function()


# Built-in Scope = print(), len(), and other standard functions and types

# # NOTES:-
# Local Scope: Variables defined inside a function; accessible only within that function.
# Global Scope: Variables defined outside any function; accessible anywhere in the code.
# Enclosing Scope: Variables in the local scope of enclosing functions; can be accessed by nested functions.
# Built-in Scope: Names that are pre-defined in Python; accessible from anywhere.
# LEGB Rule: The order in which Python looks for variable names


# SCOPE PRORGRAMMING EXAMPLE
x = "Global"
def outer_function():
    x = "Enclosing"
    def inner_function():
        x = "Local"
        print(x)  # This will print the local x
    inner_function()
    print(x)      # This will print the enclosing x
outer_function()
print(x)          # This will print the global x



# FILE HANDLING IN PYTHON
# 'r': Read = Opens the file for reading. Raises an error if the file does not exist.
# 'w': Write = Opens the file for writing. Creates a new file if it does not exist or truncates (overwrites) the file if it does.
# 'a': Append Opens = the file for appending. Creates a new file if it does not exist and does not truncate the file.
# 'b': Binary mode = Opens the file in binary mode (used for non-text files).
# 't': Text mode = Opens the file in text mode.

# Open a file for reading
file = open('example.txt', 'r')

# Reading the entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Using strip() to remove newline characters

# Writing to a file
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("Welcome to file handling in Python.\n")

# Appending to a file
with open('output.txt', 'a') as file:
    file.write("This line will be appended to the file.\n")

# Reading an image file in binary mode
with open('image.png', 'rb') as file:
    data = file.read()
    print(data)  # This will print binary data

# Closing the file
file = open('example.txt', 'r')
# Perform file operations
file.close()  # Always remember to close the file

# Handling Exceptions
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("An error occurred while reading the file.")

# Delete a file
import os
try:
    os.remove('output.txt')
    print("File deleted successfully")
except FileNotFoundError:
    print("The file does not exist.")


# LEARN MODULES :
# NumPy
# Pandas
# Matplotlib
# Scikit-learn
# MongoDB
# Python MySQL