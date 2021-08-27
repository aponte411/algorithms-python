from typing import List


def search_insert(nums: List[int], target: int) -> List[int]:
    """O(log n) time O(1)"""
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = left + ((right - left)//2)
        if nums[pivot] == target:
            return pivot
        elif nums[pivot] > target:
            right = pivot
        else:
            left = pivot + 1
    return left

def main():
    nums = [1,3,5,6]
    target = 5
    result = search_insert(nums, target)
    expected = 2
    assert result == expected
    print(result)

if __name__ == '__main__':
    main()
