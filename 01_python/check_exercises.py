"""Checks your answers in exercises.py.

Usage:
    python check_exercises.py              # check exercises.py
    python check_exercises.py --solutions  # check the reference solutions
"""

import sys

if "--solutions" in sys.argv:
    from solutions import exercises_solutions as ex
else:
    import exercises as ex


def _raises(func, *args):
    try:
        func(*args)
    except ValueError:
        return True
    return False


CHECKS = {
    "celsius_to_fahrenheit": lambda: ex.celsius_to_fahrenheit(100) == 212
    and ex.celsius_to_fahrenheit(-40) == -40,
    "split_minutes": lambda: ex.split_minutes(135) == (2, 15)
    and ex.split_minutes(59) == (0, 59),
    "initials": lambda: ex.initials("ada lovelace") == "A.L."
    and ex.initials("Guido van Rossum") == "G.V.R.",
    "is_palindrome": lambda: ex.is_palindrome("Never odd or even")
    and not ex.is_palindrome("backend"),
    "mask_email": lambda: ex.mask_email("paras@example.com") == "p****@example.com",
    "second_largest": lambda: ex.second_largest([4, 9, 9, 2]) == 4
    and ex.second_largest([1, 2]) == 1,
    "chunk": lambda: ex.chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    and ex.chunk([], 3) == [],
    "grade": lambda: [ex.grade(s) for s in (95, 80, 79, 60, 12)] == ["A", "B", "C", "D", "F"]
    and _raises(ex.grade, 101)
    and _raises(ex.grade, -1),
    "status_message": lambda: [ex.status_message(c) for c in (200, 301, 404, 503, 99)]
    == ["success", "redirect", "client error", "server error", "unknown"],
    "fizzbuzz": lambda: ex.fizzbuzz(15)
    == [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"],
    "count_vowels": lambda: ex.count_vowels("Backend Developer") == 6
    and ex.count_vowels("xyz") == 0,
    "first_negative_index": lambda: ex.first_negative_index([3, 0, -2, -5]) == 2
    and ex.first_negative_index([1, 2]) == -1,
    "apply_discount": lambda: ex.apply_discount(200) == 180.0
    and ex.apply_discount(99.99, 15) == 84.99
    and ex.apply_discount(10, 33, round_to=0) == 7.0,
    "word_frequencies": lambda: ex.word_frequencies("the cat and The hat")
    == {"the": 2, "cat": 1, "and": 1, "hat": 1},
    "compose": lambda: ex.compose(lambda x: x + 1, lambda x: x * 2)(5) == 11,
}


def main():
    passed = 0
    for name, check in CHECKS.items():
        try:
            ok = bool(check())
            detail = ""
        except Exception as e:  # show what went wrong instead of crashing
            ok = False
            detail = f"  ({type(e).__name__}: {e})"
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {name}{detail}")
    print(f"\n{passed}/{len(CHECKS)} passed")
    return 0 if passed == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
