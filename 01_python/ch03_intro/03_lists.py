"""Chapter 3.1.3: Lists.

Run: python 03_lists.py
"""

squares = [1, 4, 9, 16, 25]
print(squares)

# Indexing and slicing work like strings
print(squares[0], squares[-1])   # 1 25
print(squares[-3:])              # [9, 16, 25]

# Concatenation
print(squares + [36, 49])

# Lists are MUTABLE (unlike strings)
cubes = [1, 8, 27, 65, 125]      # oops, 4**3 is 64
cubes[3] = 64
cubes.append(216)
print(cubes)

# Assigning to slices
letters = ["a", "b", "c", "d", "e", "f", "g"]
letters[2:5] = ["C", "D", "E"]   # replace
print(letters)
letters[2:5] = []                # remove
print(letters)
letters[:] = []                  # clear
print(letters)

# Aliasing gotcha: two names, ONE list
rgb = ["Red", "Green", "Blue"]
rgba = rgb
rgba.append("Alpha")
print(rgb)                       # Alpha shows up here too!
copy = rgb[:]                    # a slice makes a (shallow) copy
copy.append("Extra")
print(rgb, copy)

# Common methods
nums = [5, 2, 9, 1]
nums.insert(0, 7)     # [7, 5, 2, 9, 1]
nums.remove(9)        # removes first 9
last = nums.pop()     # removes and returns last item -> 1
nums.sort()           # in place
print(nums, last, len(nums))
print(sorted([3, 1, 2], reverse=True))  # returns a NEW list
print(nums.index(5), 5 in nums, sum(nums), max(nums), min(nums))

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[1][2])   # 6

# List comprehension (preview of chapter 5)
print([n * n for n in range(6)])
