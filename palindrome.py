# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.


def is_palindrome(x):
    return str(x) == str(x)[::-1]



print(is_palindrome(123454300))
print(is_palindrome(1234321))
print(is_palindrome(1000001))
print(is_palindrome(-1524))
print(is_palindrome(-12321))
print(is_palindrome(-100))