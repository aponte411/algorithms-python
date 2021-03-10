import pytest

def longest_palindrome(s: str) -> str:
    """
    Time: O(n^2) worst case, O(n) best case
    Space: O(1)
    """
    if len(s) <= 1:
        return s
    result = ""
    for idx in range(len(s)):
        # odds: center is idx
        left = right = idx
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # update the largest string
            if right - left + 1 > len(result):
                result = s[left:right+1]
            left -= 1
            right += 1
        # evens
        left, right = idx, idx+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(result):
                result = s[left:right+1]
            left -= 1
            right += 1
    return result

@pytest.mark.parametrize(
    "input, expected",
    [("babad", "bab"), ("cbbd", "bb"), ("a", "a")]
)
def test(input, expected):
    result = longest_palindrome(s=input)
    assert result == expected

pytest.main()

