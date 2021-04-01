from collections import Counter
from typing import List
import pytest

def largest_unique_number(A: List[int]) -> int:
    counts = Counter(A)
    max_val = 0
    at_least_1 = False
    for integer, count in counts.most_common():
        if count == 1:
            max_val = max(max_val, integer)
            at_least_1 = True
        else:
            continue

    return max_val if at_least_1 else -1

def test():
    A = [5,7,3,9,4,9,8,3,1]
    expected = 8
    result = largest_unique_number(A)
    assert result == expected

pytest.main()
