# Like vegetables, we have different data types in Python.
# The most common ones are int, float, str, and bool.

# A variable is a named location in memory that can store a value.
# In Python, the type is inferred from the value assigned.

# Integer is a full number, float is a decimal number,
# str is a string of characters, bool is a boolean value (True or False).

integer_value = 10
float_value = 3.14
string_value = "hello"
boolean_value = True

print("integer_value:", integer_value, type(integer_value))
print("float_value:", float_value, type(float_value))
print("string_value:", string_value, type(string_value))
print("boolean_value:", boolean_value, type(boolean_value))

# Simple examples using these values
print("sum:", integer_value + 5)
print("average:", (integer_value + float_value) / 2)
print("message:", string_value + " world")
print("is positive:", integer_value > 0)
print("is long text:", len(string_value) > 4)


