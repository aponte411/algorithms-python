from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    """O(n) time, O(n) space"""
    n = len(nums)
    left, right = 0, n - 1
    result = [0 for i in range(n)]
    i = n - 1
    while i >= 0:
        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1
        else:
            square = nums[left]
            left += 1
        result[i] = square * square
        i -= 1
    return result


def main():
    nums = [-4,-1,0,3,10]
    result = sorted_squares(nums)
    expected = [0,1,9,16,100]
    assert result == expected
    print(result)


if __name__ == '__main__':
    main()
