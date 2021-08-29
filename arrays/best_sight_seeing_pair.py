import pytest
from typing import List

def best_sight_seeing_pair(values: List[int]) -> int:
    """
    We want to find the best score for a pair of values.
    The scoring function = i < j = A[i] + A[j] + i - j.
    To get the max A[i] + i + A[j] - j , we need to keep track of the
    best A[i] + i.
    """
    A_i = values[0]
    max_score = 0
    for j in range(1, len(values)):
        A_j = values[j]
        max_score = max(max_score, A_i + A_j - j)
        A_i = max(A_i, A_j + j)
    return max_score

@pytest.mark.parametrize(
    "inputs, expected",
    [([8,1,5,2,6], 11), ([1,2], 2)]
)
def test_best_sight_seeing_pair(inputs, expected):
    result = best_sight_seeing_pair(values=inputs)
    assert result == expected

pytest.main()


