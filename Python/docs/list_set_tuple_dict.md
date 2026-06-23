# Python Collection Types

## Quick comparison

| Type       | Symbol        | Ordered | Changeable | Duplicate? |
|------------|---------------|:-------:|:----------:|:----------:|
| List       | `[]`          | Yes     | Yes        | Yes        |
| Set        | `set()` / `{}`| No      | Yes        | No         |
| Tuple      | `()`          | Yes     | No         | Yes        |
| Dictionary | `{}`          | Yes*    | Yes        | Keys: No   |

> *Dictionaries preserve insertion order in Python 3.7+.

## Simple and short explanations

### List
- A list is a collection of items in order.
- You can change items, add or remove values.
- Duplicates are allowed.
- Example: favorites or steps in a sequence.

### Set
- A set stores unique values with no order.
- Use it when duplicates are not allowed.
- Good for membership tests and removing repeated items.
- Example: unique tags or IDs.

### Tuple
- A tuple is like a list, but fixed.
- Once created, you cannot change its items.
- It keeps order and can contain duplicates.
- Example: coordinates or a record with fixed fields.

### Dictionary
- A dictionary stores pairs of `key: value`.
- Keys are unique, values can repeat.
- Items are ordered by insertion order in modern Python.
- Example: a contact list with names and phone numbers.

## Example code

```python
# List
fruits = ["apple", "banana", "apple"]
print(fruits)
print(fruits[1])
fruits.append("orange")
print("after append:", fruits)

# Set
colors = {"red", "blue", "green", "blue"}
print(colors)
print("has red?", "red" in colors)

# Tuple
point = (10, 20)
print(point)
print("x:", point[0])

# Dictionary
person = {"name": "Sara", "age": 25}
print(person)
print("name:", person["name"])
person["city"] = "Paris"
print(person)
```
