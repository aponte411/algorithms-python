import pytest

def non_repeating_substring(s: str) -> int:
    window_start = 0
    max_length = 0
    char_idx_map = {}
    for window_end in range(len(s)):
        right_char = s[window_end]
        # if weve seen this char before we need to shrink the
        # window.
        if right_char in char_idx_map:
            # the end of the window is the index thats further
            # max(window_start, last_right_char_idx + 1)
            window_start = max(window_start, char_idx_map[right_char] + 1)
        # if not save the idx
        char_idx_map[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

def test1():
    str1 = "aabccbb"
    expected = 3
    result = non_repeating_substring(s=str1)
    assert result == expected

pytest.main()
