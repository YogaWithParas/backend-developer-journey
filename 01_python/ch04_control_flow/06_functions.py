"""Chapter 4.8-4.9: Defining functions.

Run: python 06_functions.py
"""


# --- Basic function with a docstring and a return value ---------------------
def fib(n):
    """Return a list of Fibonacci numbers less than n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


print(fib(100))
print(fib.__doc__)

# A function with no return statement returns None
def greet(name):
    print(f"Hello, {name}!")


print(greet("Paras"))   # prints the greeting, then None


# --- Default argument values -----------------------------------------------
def connect(host, port=5432, timeout=30):
    return f"connecting to {host}:{port} (timeout {timeout}s)"


print(connect("localhost"))
print(connect("db.example.com", 6543))
print(connect("db.example.com", timeout=5))   # keyword argument


# GOTCHA: default values are evaluated ONCE. Never use a mutable default.
def bad_append(item, items=[]):
    items.append(item)
    return items


def good_append(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


print(bad_append(1), bad_append(2))    # [1, 2] [1, 2]  <- shared list!
print(good_append(1), good_append(2))  # [1] [2]


# --- *args and **kwargs ----------------------------------------------------
def total(*numbers):
    """Accept any number of positional arguments (a tuple)."""
    return sum(numbers)


def build_url(base, **params):
    """Accept any number of keyword arguments (a dict)."""
    query = "&".join(f"{k}={v}" for k, v in params.items())
    return f"{base}?{query}" if query else base


print(total(1, 2, 3, 4))
print(build_url("/users", page=2, limit=20))

# Unpacking arguments
values = [3, 4]
print(pow(*values))                    # same as pow(3, 4)
opts = {"port": 8080, "timeout": 1}
print(connect("api.local", **opts))


# --- Positional-only (/) and keyword-only (*) parameters --------------------
def create_user(username, /, *, is_admin=False):
    return f"{username} (admin={is_admin})"


print(create_user("paras", is_admin=True))
# create_user(username="paras")   # TypeError: positional-only
# create_user("paras", True)      # TypeError: keyword-only


# --- Lambda: small anonymous functions -------------------------------------
pairs = [(1, "one"), (3, "three"), (2, "two")]
pairs.sort(key=lambda pair: pair[1])   # sort by the text
print(pairs)


def make_multiplier(n):
    return lambda x: x * n            # a function that returns a function


double = make_multiplier(2)
print(double(21))


# --- Type hints (optional, but standard in modern backend code) -------------
def average(scores: list[float]) -> float:
    """Return the mean of scores, or 0.0 for an empty list."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


print(average([90, 80, 70]))
