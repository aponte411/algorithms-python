import pytest
from typing import Dict
from collections import OrderedDict


def longest_substring_with_k_distinct_chars_v2(s: str, k: int) -> int:
    """
    Use a sliding window and an OrderedDict to get the leftmost (top of the queue)
    char
    """
    if k == 0 or len(s) == 0:
        return 0
    ans = 0
    # sliding window pointers
    start, end = 0, 0
    char_idx_map = OrderedDict()
    ans = 1
    while end < len(s):
        char = s[end]
        if char in char_idx_map:
            del char_idx_map[char]
        # store in the end index
        char_idx_map[char] = end
        end += 1
        if len(char_idx_map) > k:
            # use FIFO to get the leftmost char
            _, idx = char_idx_map.popitem(last=False)
            # move the window forward
            start = idx + 1
        ans = max(ans, end - start)
    return ans

def longest_substring_with_k_distinct_chars_v1(s: str, k: int) -> int:
    """
    Use a sliding window approach and a dictionary to keep track of
    the counts.
    1. Insert characters into the map until we have K distinct chars.
    2. these chars constitute our sliding window so we can use the difference between the
    start and end (window size) to get the current substring size, and update the longest weve seen thus far
    3. At each step when we try to shrink the window from the beginning (start), if the count is larger than K.
    4. While shrinking we decrement the char count and when the count is zero, we remove it from the list.
    """
    char_counts: Dict[str, int] = {}
    window_start = 0
    longest_subtring = 0
    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in char_counts:
            char_counts[right_char] = 0
        char_counts[right_char] += 1
        # Shrink the window if were more than k
        # distinct chars
        while len(char_counts) > k:
            left_char = s[window_start]
            # we already used this so decrement going
            # out of the window
            char_counts[left_char] -= 1
            # if our new count is zero, weve used this and can remove it
            if char_counts[left_char] == 0:
                del char_counts[left_char]
            # shrink window
            window_start += 1
        # update longest substring
        longest_substring = max(longest_subtring, window_end - window_start + 1)

    return longest_substring


@pytest.mark.parametrize(
    "inputs, expected",
    [(["eceba", 2],3),(["aa",1], 2)]
)
def testv1(inputs, expected):
    result = longest_substring_with_k_distinct_chars_v1(s=inputs[0], k=inputs[1])
    assert result == expected

@pytest.mark.parametrize(
    "inputs, expected",
    [(["eceba", 2],3),(["aa",1], 2)]
)
def testv2(inputs, expected):
    result = longest_substring_with_k_distinct_chars_v2(s=inputs[0], k=inputs[1])
    assert result == expected


pytest.main()
