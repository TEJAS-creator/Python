# CREATING A MODULE
# mymodule.py
def greet(name):
    return f"Hello, {name}!"
def add(a, b):
    return a + b


# Importing a Module
# main.py
import mymodule
print(mymodule.greet("Alice"))  # Output: Hello, Alice!
print(mymodule.add(5, 3))        # Output: 8


# Importing Specific Functions
from mymodule import greet
print(greet("Bob"))  # Output: Hello, Bob!


# Importing All Functions
# To import all functions from a module, use the * operator
from mymodule import *
print(add(10, 20))  # Output: 30


# Built-in Modules
import math
print(math.sqrt(16))  # Output: 4.0

import random
print(random.randint(1, 10))  # Output: Random number between 1 and 10

import datetime
now = datetime.datetime.now()
print(now)  # Output: Current date and time

import os
print(os.getcwd())  # Output: Current working directory


# Creating a Package
# mypackage/
#     __init__.py
#     module1.py
#     module2.py

from mypackage import module1 # TO IMPORT A MODULE FROM HE PACKAGE
from mypackage.module1 import function_name # TO IMPORT A PARTICULAR FUNCTION FROM A MODULE IN A PACKAGE


# Installing Third-Party Modules
# pip install module_name

