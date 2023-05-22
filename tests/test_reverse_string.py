import pytest

from reverse_string.reverse_string import reverse_string

def test_reversed_string_with_cat():
    assert reverse_string("cat") == "tac"
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""