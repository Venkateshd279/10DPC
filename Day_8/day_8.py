# function 
# using logic to perform a specific task is called function.

def add(a,b):
    return a + b


print(add(5,10))
print(add(20,30))

def multiply(x,y):
    return x * y

print(multiply(20,33))
print(multiply(88,90))

def greet(name):
    print ("Hello", name)

greet("John")


def calculate_percentage(marks, total_marks):
    percentage = (marks / total_marks) * 100
    print ("Your percentage is:", percentage)

calculate_percentage(85, 100)

# create calculator function

def add(num1, num2):
    return num1 + num2 

def subtract(num1, num2):
    return num1 - num2 

def multiply(num1, num2):
    return num1 * num2 

def divide(num1, num2):
    return num1 / num2

print(add(10,5))
print(subtract(10,5))
print(multiply(10,5))
print(divide(10,5))
