

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def is_palindrome(word):
    """Check if a word or phrase is a palindrome."""
    word = word.lower().replace(" ", "")
    return word == word[::-1]
