import pytest

from valid_palindrome.valid_palindrome import valid_palindrome

def test_valid_palindrome():
    assert valid_palindrome("level") == True
    assert valid_palindrome("algorithm") == False
    assert valid_palindrome("A man, a plan, a canal: Panama.") == True