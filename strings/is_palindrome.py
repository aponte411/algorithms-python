import pytest

def is_palindrome(s: str) -> bool:
    left, right = 0, len(s)-1
    while left < right:
        # move forward is its not [azAZ]
        while left < right and not s[left].isalnum():
            left+=1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


@pytest.mark.parametrize(
    "input, expected",
    [("abc", False),("aba", True)]
)
def test(input, expected):
    result = is_palindrome(input)
    assert result == expected

pytest.main()

