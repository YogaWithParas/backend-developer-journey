"""Reference solutions. Try the exercises yourself before reading these!"""


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def split_minutes(total_minutes):
    return total_minutes // 60, total_minutes % 60


def initials(full_name):
    return "".join(part[0].upper() + "." for part in full_name.split())


def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def mask_email(email):
    user, domain = email.split("@")
    return user[0] + "*" * (len(user) - 1) + "@" + domain


def second_largest(numbers):
    distinct = sorted(set(numbers))
    return distinct[-2]


def chunk(items, size):
    return [items[i:i + size] for i in range(0, len(items), size)]


def grade(score):
    if not 0 <= score <= 100:
        raise ValueError(f"score must be 0-100, got {score}")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


def status_message(code):
    match code // 100:
        case 2:
            return "success"
        case 3:
            return "redirect"
        case 4:
            return "client error"
        case 5:
            return "server error"
        case _:
            return "unknown"


def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result


def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count


def first_negative_index(numbers):
    for i, n in enumerate(numbers):
        if n < 0:
            return i
    return -1


def apply_discount(price, percent=10, *, round_to=2):
    return round(price * (100 - percent) / 100, round_to)


def word_frequencies(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def compose(f, g):
    def h(x):
        return f(g(x))
    return h
