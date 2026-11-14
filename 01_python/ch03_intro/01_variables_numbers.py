"""Chapter 3.1: Variables and numbers.

Run: python 01_variables_numbers.py
"""

# --- Variables -------------------------------------------------------------
# A variable is a name that points to a value. No type declaration needed.
width = 20
height = 5 * 9
print("area:", width * height)          # 900

# Names can be re-bound to values of a different type
x = 10
x = "now I'm a string"
print(x, type(x))

# Multiple assignment and swapping
a, b = 1, 2
a, b = b, a
print("swapped:", a, b)                  # 2 1

# Naming convention in Python: snake_case
user_count = 3
MAX_RETRIES = 5                          # ALL_CAPS = "treat as a constant"

# --- Numbers ---------------------------------------------------------------
print(2 + 2)        # 4      int
print(50 - 5 * 6)   # 20     normal precedence: * before -
print((50 - 5) * 6) # 270
print(8 / 5)        # 1.6    / always gives a float
print(17 // 3)      # 5      floor division
print(17 % 3)       # 2      remainder (modulo)
print(5 ** 2)       # 25     power
print(-7 // 2)      # -4     floor rounds DOWN, not towards zero

# Mixing int and float gives float
print(4 * 3.75 - 1)  # 14.0

# Floats are approximations
print(0.1 + 0.2)          # 0.30000000000000004
print(round(0.1 + 0.2, 2))  # 0.3

# Converting between types
print(int("42") + 1)     # 43
print(float("3.5"))      # 3.5
print(str(99) + " bottles")

# Augmented assignment
total = 0
total += 10
total *= 2
print("total:", total)   # 20

# Big integers are fine in Python
print(2 ** 100)
