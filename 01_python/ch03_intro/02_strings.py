"""Chapter 3.1.2: Text (strings).

Run: python 02_strings.py
"""

# --- Creating strings ------------------------------------------------------
single = 'spam eggs'
double = "doesn't need escaping"
escaped = 'doesn\'t'                     # backslash escapes the quote
print(single, "|", double, "|", escaped)

print("First line.\nSecond line.")       # \n = newline
print(r"C:\some\name")                   # raw string: backslashes kept as-is

multi = """\
Usage: app [OPTIONS]
     -h        Show help
     -v        Verbose
"""
print(multi)

# --- Concatenation and repetition ------------------------------------------
print(3 * "un" + "ium")                  # unununium
print("Py" "thon")                       # adjacent literals auto-join

# --- Indexing (0-based) ----------------------------------------------------
word = "Python"
print(word[0], word[5])                  # P n
print(word[-1], word[-2])                # n o   (negative = from the end)

# --- Slicing [start:end]  (end is NOT included) ----------------------------
print(word[0:2])     # Py
print(word[2:5])     # tho
print(word[:2])      # Py      (start defaults to 0)
print(word[4:])      # on      (end defaults to len)
print(word[-2:])     # on
print(word[::-1])    # nohtyP  (step -1 reverses)
print(word[:2] + word[2:])  # always equals word

# Out-of-range slices are forgiving; out-of-range indexes are not
print(word[4:42])    # on
# print(word[42])    # IndexError

# --- Strings are immutable -------------------------------------------------
# word[0] = "J"      # TypeError
print("J" + word[1:])                    # Jython (build a new string instead)

print(len("supercalifragilisticexpialidocious"))  # 34

# --- f-strings (formatting) ------------------------------------------------
name, age, balance = "Paras", 30, 1234.5
print(f"{name} is {age} years old")
print(f"Balance: ${balance:,.2f}")       # Balance: $1,234.50
print(f"{name!r:>10}|")                  # right-align in width 10

# --- Useful methods --------------------------------------------------------
s = "  Hello, Backend World  "
print(s.strip())                  # remove surrounding whitespace
print(s.lower(), s.upper())
print(s.strip().split(", "))      # ['Hello', 'Backend World']
print("-".join(["a", "b", "c"]))  # a-b-c
print(s.replace("World", "Dev"))
print("Backend" in s)             # True
print(s.strip().startswith("Hello"), s.count("l"))
