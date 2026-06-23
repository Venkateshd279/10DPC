# List, Set, Tuple, and Dictionary in Python

# Simple examples for each type

# List
fruits = ["apple", "banana", "apple"]
print("List:", fruits)
print("Second item:", fruits[1])
fruits.append("orange")
print("After append:", fruits)

print()

# Set
colors = {"red", "blue", "green", "blue"}
print("Set:", colors)
print("Has red?", "red" in colors)

print()

# Tuple
point = (10, 20)
print("Tuple:", point)
print("X coordinate:", point[0])

print()

# Dictionary
person = {"name": "Sara", "age": 25}
print("Dictionary:", person)
print("Name:", person["name"])
person["city"] = "Paris"
print("After add city:", person)
