# Day 5: Lists and List Operations

## Overview
Lists are one of the most commonly used data structures in Python. They allow you to store multiple items in a single variable and perform various operations on them.

## Basic List Creation and Indexing

```python
task = ['eat', 'sleep', 'code', 'repeat']
print("Before append:", task)
```
**Output:** `Before append: ['eat', 'sleep', 'code', 'repeat']`

- Lists are created using square brackets `[]`
- Elements are separated by commas
- Lists can contain strings, numbers, or mixed data types

---

## List Operations

### 1. **append()** - Add Single Element
```python
task.append('fun')
print("After append:", task)
```
**Output:** `After append: ['eat', 'sleep', 'code', 'repeat', 'fun']`

- Adds a single element to the end of the list
- Modifies the original list

### 2. **Iterating Through List with Conditional Logic**
```python
for i in task:
    print(i)
    if i == 'eat':
        print("sleep well")
    elif i == 'code':
        print("code well")
    elif i == 'fun':
        print("have fun")
    else:
        print("repeat well")
```
**Output:**
```
eat
sleep well
code
code well
repeat
repeat well
fun
have fun
```

- Loops through each element in the list
- Uses conditional statements to perform different actions based on element values

### 3. **clear()** - Remove All Elements
```python
task.clear()
print("After clear:", task)
```
**Output:** `After clear: []`

- Removes all elements from the list
- List becomes empty but still exists

### 4. **copy()** - Create a Copy of the List
```python
task.copy()
print("After copy:", task)
```
**Output:** `After copy: []`

- Creates a shallow copy of the list
- Useful for creating independent duplicates

### 5. **count()** - Count Occurrences
```python
task.count('eat')
print("After count:", task.count('eat'))
```
**Output:** `After count: 0` (since list was cleared earlier)

- Returns the number of times a specified element appears in the list
- Returns 0 if element is not found

### 6. **extend()** - Add Multiple Elements
```python
task.extend(['eat', 'sleep', 'code', 'repeat'])
print("After extend:", task)
```
**Output:** `After extend: ['eat', 'sleep', 'code', 'repeat']`

- Adds multiple elements from an iterable to the end of the list
- Different from `append()` which adds a single item

### 7. **index()** - Find Element Position
```python
task.index('code')
print("After index:", task.index('code'))
```
**Output:** `After index: 2`

- Returns the index (position) of the first occurrence of a specified element
- Raises an error if element is not found

### 8. **insert()** - Add Element at Specific Position
```python
task.insert(2, 'think well before you code')
print("After insert:", task)
```
**Output:** `After insert: ['eat', 'sleep', 'think well before you code', 'code', 'repeat']`

- Inserts an element at a specified index position
- Shifts existing elements to the right

### 9. **pop()** - Remove Last Element
```python
task.pop()
print("After pop:", task)
```
**Output:** `After pop: ['eat', 'sleep', 'think well before you code', 'code']`

- Removes and returns the last element in the list
- Can also specify an index: `pop(index)`

### 10. **remove()** - Remove Specific Element
```python
task.remove('eat')
print("After remove:", task)
```
**Output:** `After remove: ['sleep', 'think well before you code', 'code']`

- Removes the first occurrence of a specified element
- Raises an error if element is not found

### 11. **reverse()** - Reverse List Order
```python
task.reverse()
print("After reverse:", task)
```
**Output:** `After reverse: ['code', 'think well before you code', 'sleep']`

- Reverses the order of elements in the list
- Modifies the original list

### 12. **sort()** - Sort List Alphabetically
```python
task.sort()
print("After sort:", task)
```
**Output:** `After sort: ['code', 'sleep', 'think well before you code']`

- Sorts elements in alphabetical (or numerical) order
- Modifies the original list
- For descending order, use `reverse=True` parameter

---

## Summary of List Methods

| Method | Description |
|--------|-------------|
| `append()` | Add single element to end |
| `clear()` | Remove all elements |
| `copy()` | Create a shallow copy |
| `count()` | Count occurrences of element |
| `extend()` | Add multiple elements |
| `index()` | Find index of element |
| `insert()` | Add element at specific position |
| `pop()` | Remove and return last element |
| `remove()` | Remove specific element |
| `reverse()` | Reverse list order |
| `sort()` | Sort list alphabetically |

---

## Key Takeaways
- Lists are **mutable** (can be modified after creation)
- Most list methods **modify the original list** (except `count()`, `index()`, and `copy()`)
- Understanding these operations is crucial for effective list manipulation in Python
- Lists form the foundation for working with collections of data
