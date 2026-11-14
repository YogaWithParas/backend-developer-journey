"""Chapter 4.1: if statements (+ 4.7 match).

Run: python 04_conditionals.py
"""


def describe(x):
    if x < 0:
        return "negative"
    elif x == 0:
        return "zero"
    elif x == 1:
        return "single"
    else:
        return "more"


for value in (-5, 0, 1, 42):
    print(value, "->", describe(value))

# Comparison operators: == != < <= > >=
# Boolean operators: and, or, not
age = 25
has_id = True
if age >= 18 and has_id:
    print("allowed in")

# Chained comparisons
score = 72
if 70 <= score < 80:
    print("grade C")

# Truthiness: these are all "falsy" -> 0, 0.0, "", [], {}, None, False
for thing in (0, "", [], None, "hi", [0], 3):
    print(repr(thing), "is", "truthy" if thing else "falsy")

# Conditional (ternary) expression
status_code = 404
label = "ok" if status_code < 400 else "error"
print(label)

# is vs == : use `is` only for None / True / False
result = None
if result is None:
    print("no result yet")


# match (Python 3.10+) - structural pattern matching
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 400 | 422:
            return "Bad request"
        case 404:
            return "Not found"
        case _:                          # wildcard = default
            return "Something else"


print(http_status(200), http_status(422), http_status(500))


def handle(command):
    match command.split():
        case ["get", key]:
            return f"GET {key}"
        case ["set", key, value]:
            return f"SET {key}={value}"
        case _:
            return "unknown command"


print(handle("get user"), "|", handle("set user paras"), "|", handle("dance"))
