# Loops in python
# A loop is used to repeat a block of code multiple times. Python has two main types of loops: for loops and while loops.
# for loop we use when we need fixed number of iterations, 

# using range() function to generate a sequence of numbers
for i in range(5):  # This will iterate from 0 to 4
    print("Iteration:", i)

# while loop we use when we need to repeat a block of code until a certain condition is met.
count = 0
while count < 5:  # This will continue until count is no longer less than 5
    print("Count:", count)
    count += 1  # Increment count to avoid infinite loop
