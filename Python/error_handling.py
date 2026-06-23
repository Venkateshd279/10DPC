# Error Handling in Python
# when program crashes it will show error message, to show friendly manner we use error handling in python.

# try block is used to test a block of code for errors.

"""
try -> write code might cause error
except -> handle the error
else -> if no error occurs
finally -> code will run no matter what

"""
try:
    # code that may raise an exception
    result = int(10 / 0 ) # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # code to handle the exception
    print("Error: Division by zero is not allowed.")
except Exception as e:
    # code to handle any other exceptions
    print(f"An error occurred: {e}")
else:
    # code to execute if no exceptions were raised
    print("The code is successful, result is:", result)
finally:
    # code that will run regardless of whether an exception occurred or not
    print("This always runs.")

# use expcept with exception as e to get the error message and print it in friendly manner.

try:
    # code that may raise an exception
    result = int(10 / 0 ) # This will raise a ZeroDivisionError
except Exception as e:
    # code to handle any exceptions and print the error message
    print(f"An error occurred: {e}")


try:
    # code that may raise an exception
    number = int("hello")
except Exception as e:
    # code to handle any exceptions and print the error message
    print(f"An error occurred: {e}")