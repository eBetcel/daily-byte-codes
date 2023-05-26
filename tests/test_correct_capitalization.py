import pytest

from correct_capitalization.correct_capitalization import correct_capitalization

def test_correct_capitalization():
    assert correct_capitalization("USA") == True
    assert correct_capitalization("Calvin") == True
    assert correct_capitalization("compUter") == False
    assert correct_capitalization("coding") == True