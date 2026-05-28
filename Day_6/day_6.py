# dictionary

activity = {
    "monday": "Go to the gym",
    "tuesday": "Go to the park",
    "wednesday": "Go to the library",
    "thursday": "Go to the beach",
    "friday": "Go to the movies",
    "value" : "100"}

print(activity)

print(activity["tuesday"])

#adding new key value pair

activity["saturday"] = "Go to the mall"

print(activity)

# deleting key value pair

del activity["monday"]
print(activity)

activity["sunday"] = "Go to the restaurant"

print(activity)

# add 50 with current value of key "value"


number = { "value": 100}
number["value"] += 50
print(number)


# add two dictionaries

#Example 1:

car = {"brand": "Toyota", "model": "Camry" }
owner = {"name": "John", "age": 30}

car_owner = {**car, **owner}
print(car_owner)

#Example 2:
tree = {"type": "Oak", "height": 20}
flower = {"type": "Rose", "color": "Red"}
tree_flower = {**tree, **flower}

print(tree_flower)

#Example 3:
#how to combine three dictionaries

person = {"name": "Alice", "age": 25}
coach = {"name": "Bob", "age": 40}
native = {"name": "Charlie", "age": 35}

person_coach_native = {**person, **coach, **native}
print(person_coach_native)
