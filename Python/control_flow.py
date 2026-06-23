# Python control flow statements
# Control flow statements allow you to control the execution of your code based on conditions
# Run code only if condition is met 

age = 15
if age >= 18:
    print("You are an adult.")


# if else statement
# when if condition is true run if block else run else block
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# if elif else statement
# To check many conditions we can use elif statement
age = 15
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")