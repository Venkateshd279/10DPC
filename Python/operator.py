"""Simple operator examples for learning.

This file contains runnable examples for arithmetic, comparison,
and logical operators.
"""

a = 10
b = 5

def main():
	# Arithmetic
	print(a + b)    # 15
	print(a - b)    # 5
	print(a * b)    # 50
	print(a / b)    # 2.0
	print(a // b)   # 2
	print(a % b)    # 0
	print(a ** 2)   # 100

	# Comparison
	print(a == b)   # False
	print(a != b)   # True
	print(a > b)    # True
	print(a < b)    # False

	# Logical
	is_even = (a % 2 == 0)
	is_positive = (a > 0)
	print(is_even and is_positive)  # True
	print(is_even or (b < 0))       # True
	print(not is_positive)          # False


if __name__ == "__main__":
	main()

