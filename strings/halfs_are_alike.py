import pytest

def halves_are_alike(s: str) -> bool:
    def is_vowel(char: str) -> bool:
        if char in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            return True
        return False

    mid = len(s)//2
    first_half = s[:mid]
    second_half = s[mid:]

    first_vowels = 0
    second_vowels = 0
    for first, second in zip(first_half, second_half):
        if is_vowel(first):
            first_vowels += 1
        if is_vowel(second):
            second_vowels += 1
    return first_vowels == second_vowels


def test():
    s = "MerryChristmas"
    expected = False
    result = halves_are_alike(s)
    assert result == expected

pytest.main()
