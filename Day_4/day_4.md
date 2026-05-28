# Day 4: For Loops

## Overview
For loops are used to iterate over sequences such as lists, strings, dictionaries, and ranges. They allow you to execute a block of code multiple times.

## Key Concepts

### 1. For Loop with Range

#### Example 1: Single Value Range
```python
for i in range(100, 101):
    print(i)
```
**Output:** `100`

- `range(100, 101)` generates numbers from 100 to 100 (upper bound is exclusive)
- Prints a single value: 100

#### Example 2: Range with Multiple Values
```python
for i in range(0, 100):
    print(i)
```
**Output:** Numbers 0 to 99

- `range(0, 100)` generates all numbers from 0 to 99
- Iterates 100 times, printing each number

---

### 2. For Loop with Lists

```python
list = ['a', 'b', 2, 9, 7.3]

for i in list:
    print(i)
```
**Output:**
```
a
b
2
9
7.3
```

- Iterates through each element in the list
- Can contain mixed data types (strings, integers, floats)

---

### 3. For Loop with Dictionaries

```python
dict = {"name": "venkatest", "age": 30, "city": "Chennai"}

for i in dict:
    print(i)
```
**Output:**
```
name
age
city
```

- When iterating over a dictionary, the loop iterates through keys
- To access values, use `dict[i]`

---

### 4. Converting Two Lists into a Dictionary

```python
list1 = ['name', 'age', 'city']
list2 = ['venkatesh', 30, 'Chennai']

dict = {}
for i in range(len(list1)):
    dict[list1[i]] = list2[i]
print(dict)
```
**Output:**
```python
{'name': 'venkatesh', 'age': 30, 'city': 'Chennai'}
```

- Uses `range(len(list1))` to get indices
- Pairs elements from list1 (keys) with list2 (values)
- Creates a dictionary with corresponding key-value pairs

---

## Summary
- **For loops** are powerful for automating repetitive tasks
- **range()** function provides a sequence of numbers
- **Lists** and **dictionaries** can be iterated easily
- **Index-based loops** allow manipulation and transformation of data structures
