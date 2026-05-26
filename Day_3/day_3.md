# Day 3: Conditional Statements (If, Nested If, Ternary)

## Overview
Today we learn about conditional statements in Python using three types:
1. If-Elif-Else statements
2. Nested If statements
3. Ternary operators

---

## 1. If-Elif-Else Statements

### Concept
Use `if-elif-else` to check multiple conditions and execute different code based on the score.

### Example: Grade Calculator
```python
score = int(input("Enter your score:"))

if score >= 90 and score <= 100:
    print("Your grade is A+")
elif score >= 80 and score < 90:
    print("your grade is B+")
elif score >= 70 and score < 80:
    print("your grade is C+")
elif score <= 70 and score >= 0:
    print("FAIL")
else:
    print("Invalid score")
```

### How it works:
- User enters a score
- First condition checks if score is between 90-100 → Grade A+
- Second condition checks if score is between 80-90 → Grade B+
- Third condition checks if score is between 70-80 → Grade C+
- Fourth condition checks if score is below 70 → FAIL
- If none match → Invalid score

### Output Examples:
```
Enter your score: 95
Your grade is A+

Enter your score: 85
your grade is B+

Enter your score: 150
Invalid score
```

---

## 2. Nested If Statements

### Concept
Nested if means putting an `if` statement inside another `if` statement. Useful when you need to check multiple related conditions.

### Example: Subscription and Age Based Access
```python
age = int(input("Enter your age:"))
subscribe = input("Do you have a subscription? (yes/no):")

if age >= 18:
    if subscribe == "yes":
        print("You have full access")
elif age < 18:
    if subscribe.lower() == "yes":
        print("you have limited access")
elif subscribe.lower() == "no":
    print("you have no access, get subscription")
else:
    print("you have not allowed to access")
```

### How it works:
- Check if user is 18 or older
  - If yes AND has subscription → Full access
- Check if user is less than 18
  - If yes AND has subscription → Limited access
- Check if subscription is "no" → No access message
- Otherwise → Not allowed to access

### Output Examples:
```
Enter your age: 20
Do you have a subscription? (yes/no): yes
You have full access

Enter your age: 15
Do you have a subscription? (yes/no): yes
you have limited access

Enter your age: 25
Do you have a subscription? (yes/no): no
you have no access, get subscription
```

---

## 3. Ternary Operator

### Concept
A ternary operator is a quick way to write an if-else statement in one line.

### Syntax:
```python
value_if_true if condition else value_if_false
```

### Example: Age Classification
```python
age = int(input("Enter your age:"))
status = "Adult" if age >= 18 else "Child"
print(status)
```

### How it works:
- If age is 18 or more → status = "Adult"
- Otherwise → status = "Child"
- Print the status

### Output Examples:
```
Enter your age: 20
Adult

Enter your age: 12
Child
```

---

## Key Points to Remember

✓ **Indentation matters** - Python uses indentation to define code blocks  
✓ **Colons (`:`)** are required after if, elif, and else  
✓ **`and` operator** - Both conditions must be True  
✓ **`.lower()`** converts string to lowercase for comparison  
✓ **Ternary operator** - One-line if-else for simple conditions  
✓ **Nested if** - Check multiple related conditions step by step  

---

## Comparison Operators Used

- `>=` : Greater than or equal to
- `<=` : Less than or equal to
- `>` : Greater than
- `<` : Less than
- `==` : Equal to
- `!=` : Not equal to

---

## Summary

| Type | Use When | Syntax |
|------|----------|--------|
| If-Elif-Else | Multiple conditions to check | if...elif...elif...else |
| Nested If | Conditions depend on other conditions | if...then if inside |
| Ternary | Simple one condition, one line | condition ? true_value : false_value |
