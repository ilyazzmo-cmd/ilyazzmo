from utils import add, is_palindrome

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 1  
def test_is_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("Was it a car or a cat I saw") == True

print("All tests passed!")  
