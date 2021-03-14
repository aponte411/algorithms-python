import pytest
import string

MAX_INT = 2**31

def my_atoi(s: str) -> int:
    if string == "":
        return 0
    # remove white space
    new_string = s.strip()
    sign = 1
    if new_string and new_string[0] == '-':
        sign = -1
        new_string = new_string[1:]
    elif new_string and new_string[0] == '+':
        new_string = new_string[1:]

    number = 0
    for char in new_string:
        if char.isdigit():
            # multiply the number by the base (10) and convert
            # to integer.
            number = (number*10) + string.hexdigits.index(char)
        else:
            # if not a valid digit, break out
            break
    result = (number*sign)
    if result >= MAX_INT:
        # less than max
        return MAX_INT - 1
    elif result < - MAX_INT:
        return - MAX_INT
    return result


def test_negative():
    s = "   -42"
    expected = -42
    result = my_atoi(s)
    assert result == expected

pytest.main()
