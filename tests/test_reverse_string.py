import pytest

from reverse_string.reverse_string import reverse_string

def test_reversed_string():
    assert reverse_string("Cat") == "taC"
    assert reverse_string("The Daily Byte") == "etyB yliaD ehT"
    assert reverse_string("civic") == "civic"