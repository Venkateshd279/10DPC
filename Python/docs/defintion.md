# Python Concepts — Simple & Short

## Key ideas

- **Variable**: a name that stores a value.
- **Data type**: Python figures out the type from the value.
- **Function**: use `def` to write reusable code.
- **Control flow**: decide what runs with `if`, `elif`, `else`, `for`, `while`.
- **Collection**: group values using list, set, tuple, or dictionary.
- **Module**: a Python file you can import to reuse code.

## Data types

- **int**: whole number, e.g. `10`
- **float**: decimal number, e.g. `3.14`
- **str**: text, e.g. `"hello"`
- **bool**: True or False

## Operators at a glance

- **Arithmetic**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Comparison**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical**: `and`, `or`, `not`

## Collections quick table

| Type       | Symbol      | Ordered | Changeable | Duplicate? |
|------------|-------------|:-------:|:----------:|:----------:|
| List       | `[]`        | Yes     | Yes        | Yes        |
| Set        | `set()` / `{}` | No   | Yes        | No         |
| Tuple      | `()`        | Yes     | No         | Yes        |
| Dict       | `{}`        | Yes     | Yes        | Keys: No   |

## What each collection means

- **List**: ordered and changeable. good for sequences you edit.
- **Set**: unordered and only unique values. good for removing duplicates.
- **Tuple**: ordered but fixed after creation. good for values that should not change.
- **Dictionary**: key/value pairs. keys must be unique.

## Control flow

- `if` runs code only when a condition is true.
- `elif` checks another condition if the first was false.
- `else` runs when no prior condition matched.
- `for` repeats for each item in a sequence.
- `while` repeats while a condition stays true.

## Functions

- Use `def` to define a function.
- It can take inputs (parameters) and return a result.
- Helps reuse code and keep it clean.

Example:

```python
def add(a, b):
    return a + b

print(add(2, 3))  # 5
```

## Modules

- A module is a `.py` file that holds reusable code.
- A package is a folder with Python modules inside.
- The `modules/` folder in this project is a package.
- `__init__.py` tells Python that the folder is a package.
- It can be empty when you just need the folder to be importable.

### Why `__init__.py` is empty here

- It does not have to contain code.
- Its presence lets Python load `modules` as a package.
- This is why you can do `from modules.addition import addition`.

### How `app.py` uses the module

- `app.py` imports the function `addition` from `modules/addition.py`.
- This means `app.py` can call `addition(5, 3)` even though the logic is in another file.
- This keeps code organized and easier to reuse.

```python
from modules.addition import addition

result = addition(5, 3)
print("Result of addition:", result)
```

### Simple explanation in layman terms

- `modules/` is like a folder of tools.
- `addition.py` is one tool inside that folder.
- `__init__.py` is a label that says: "this folder is a Python package." 
- If the label is empty, it still works; the folder is still a package.

## Easy recall highlights

- **Variables** store values.
- **Types** are int, float, str, bool.
- **Operators** compare, calculate, and combine.
- **Lists** change, **tuples** stay fixed.
- **Sets** remove duplicates, **dicts** map keys to values.
- **If/for/while** control what runs.
- **Functions** package logic.
- **Modules** share the logic across files.
