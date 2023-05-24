import pytest

from vacuum_cleaner_route.vacuum_cleaner_route import vacuum_cleaner_route

def test_vaccum_cleaner_route_return_to_pos():
    assert vacuum_cleaner_route("LR") == True
    assert vacuum_cleaner_route("URURD") == False
    assert vacuum_cleaner_route("RUULLDRD") == True
