"""Chapter 4.2-4.5: for, range, while, break, continue, else, pass.

Run: python 05_loops.py
"""

# --- for loops iterate over any sequence ------------------------------------
words = ["cat", "window", "defenestrate"]
for w in words:
    print(w, len(w))

# Need the index too? Use enumerate (don't do range(len(...)))
for i, w in enumerate(words, start=1):
    print(i, w)

# Loop over two lists together with zip
names = ["api", "db", "cache"]
ports = [8000, 5432, 6379]
for name, port in zip(names, ports):
    print(f"{name:<6} on port {port}")

# Loop over a dict
users = {"alice": "admin", "bob": "viewer"}
for user, role in users.items():
    print(user, "->", role)

# Don't modify a collection while looping over it; loop over a copy instead
for user, role in users.copy().items():
    if role == "viewer":
        del users[user]
print(users)

# --- range ----------------------------------------------------------------
print(list(range(5)))          # [0, 1, 2, 3, 4]
print(list(range(5, 10)))      # [5, 6, 7, 8, 9]
print(list(range(0, 10, 3)))   # [0, 3, 6, 9]
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]

# --- while loops -----------------------------------------------------------
# Fibonacci numbers below 100
a, b = 0, 1
while a < 100:
    print(a, end=" ")
    a, b = b, a + b
print()

# --- break and continue ----------------------------------------------------
for n in range(10):
    if n % 2 == 0:
        continue               # skip even numbers
    if n > 7:
        break                  # stop the loop entirely
    print("odd:", n)

# --- else on a loop: runs only if the loop did NOT break --------------------
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n // x)
            break
    else:
        print(n, "is a prime number")

# --- pass: a placeholder that does nothing ---------------------------------
for _ in range(3):
    pass                       # TODO: fill in later

# --- Nested loops: a small multiplication table ----------------------------
for row in range(1, 4):
    print(" ".join(f"{row * col:3}" for col in range(1, 6)))
