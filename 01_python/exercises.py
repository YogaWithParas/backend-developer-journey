"""Chapters 3-4 exercises.

Replace each `...` with your solution, then run:
    python check_exercises.py
"""


# ---------- Variables & numbers ----------

def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit. F = C * 9/5 + 32"""
    ...


def split_minutes(total_minutes):
    """Return (hours, minutes). split_minutes(135) -> (2, 15). Hint: // and %"""
    ...


# ---------- Strings ----------

def initials(full_name):
    """'ada lovelace' -> 'A.L.'"""
    ...


def is_palindrome(text):
    """True if text reads the same backwards, ignoring case and spaces.
    'Never odd or even' -> True"""
    ...


def mask_email(email):
    """'paras@example.com' -> 'p****@example.com' (keep first char + domain)"""
    ...


# ---------- Lists ----------

def second_largest(numbers):
    """Return the second-largest DISTINCT number. [4, 9, 9, 2] -> 4"""
    ...


def chunk(items, size):
    """Split a list into chunks. chunk([1,2,3,4,5], 2) -> [[1,2],[3,4],[5]]"""
    ...


# ---------- Conditionals ----------

def grade(score):
    """90+ 'A', 80+ 'B', 70+ 'C', 60+ 'D', else 'F'.
    Raise ValueError if score is not between 0 and 100."""
    ...


def status_message(code):
    """2xx -> 'success', 3xx -> 'redirect', 4xx -> 'client error',
    5xx -> 'server error', anything else -> 'unknown'."""
    ...


# ---------- Loops ----------

def fizzbuzz(n):
    """Return a list for 1..n: 'Fizz' if divisible by 3, 'Buzz' by 5,
    'FizzBuzz' by both, otherwise the number itself (as an int)."""
    ...


def count_vowels(text):
    """Number of vowels (a, e, i, o, u), case-insensitive."""
    ...


def first_negative_index(numbers):
    """Index of the first negative number, or -1 if there is none.
    Use a loop with break (or return)."""
    ...


# ---------- Functions ----------

def apply_discount(price, percent=10, *, round_to=2):
    """Return price reduced by percent, rounded to round_to decimals.
    apply_discount(200) -> 180.0 ; apply_discount(99.99, 15) -> 84.99"""
    ...


def word_frequencies(text):
    """Return a dict of lowercase word -> count. Ignore case.
    'the cat and The hat' -> {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}"""
    ...


def compose(f, g):
    """Return a NEW function h where h(x) == f(g(x))."""
    ...
