
"""
Python function (simple and short):

A function is a block of code that performs a specific task.

We write it once and can use it multiple times.

Key words: def 

Example:

def add(a, b):
	return a + b

result = add(2, 3)  # result is 5
"""

def multiply(a,b):
    c = a * b
    return c

result = multiply(4,5)
print("result:", result)  # result is 20    

# function with parameters and default values
def greet(name="User"):
    return f"Hello, {name}!"

# function with return value
message = greet("Alice")
print(message)  # Output: Hello, Alice!

# function calculate aread of rectangle
def area_of_rectangle(length, width):
    area = length * width
    return area

# function call
result = area_of_rectangle(5, 3)
print("Area of rectangle:", result)  # Output: Area of rectangle: 15

#key points to remember about functions in Python:
# 1. Functions are defined using the def keyword.
# 2. Functions can take parameters (inputs) and return values (outputs).
# 3. Functions help in code reusability and organization.   
