import pytest
import string

def title_to_number(column_title: str) -> int:
    # initialize number
    number = 0
    # go through char by char
    for char in column_title:
        # convert char to integer using ASCII uppercase
        char_int = string.ascii_uppercase.index(char)
        # multiply number by base and add to char_int
        number = (number*26) + char_int + 1 # since A is 1
    return number

def test1():
    column_title = "ZZ"
    result = title_to_number(column_title)
    expected = 702
    assert result == expected

pytest.main()
