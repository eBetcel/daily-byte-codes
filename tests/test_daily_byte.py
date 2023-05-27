import pytest

from daily_btye.daily_byte import sum_bytes

def test_sum_bytes():
    assert sum_bytes("100", "1") == '101'
    assert sum_bytes("11", "1") == '100'
    assert sum_bytes("1", "0") == '1'