import pytest
import string

def convert_to_title(column_number: int) -> str:
    res = []
    x = column_number
    while x:
        res.append(string.ascii_uppercase[(x-1)%26])
        x = (x-1)//26
    res.reverse()
    return "".join(res)

def test1():
    column_number = 28
    expected = 'AB'
    result = convert_to_title(column_number)
    assert result == expected

pytest.main()
