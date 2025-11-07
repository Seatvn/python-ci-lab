from main import is_palindrome

def test_palindrome_true():
    assert is_palindrome("Level")

def test_palindrome_false():
    assert not is_palindrome("Python")
