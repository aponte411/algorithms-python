import pytest
from typing import List


def max_abs_val_expression(arr1: List[int], arr2: List[int]) -> int:
    """
    |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
    return the maximum value of the expression.
    """
    # Find the sum of all arrays for each index
    a = [arr1[i] + arr2[i] + i for i in range(len(arr1))]
    b = [arr1[i] + arr2[i] - i for i in range(len(arr1))]
    c = [arr1[i] - arr2[i] + i for i in range(len(arr1))]
    d = [arr1[i] - arr2[i] - i for i in range(len(arr1))]
    return max(map(lambda x: max(x)-min(x), (a,b,c,d)))


def test_max_abs_val_expression():
    arr1 = [1,2,3,4]
    arr2 = [-1,4,5,6]
    expected = 13
    result = max_abs_val_expression(arr1, arr2)
    print(result)
    assert result == expected

pytest.main()



