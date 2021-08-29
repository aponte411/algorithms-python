from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:

    left, right = 0, len(nums) - 1
    while left < right:
        twoSum = nums[left] + nums[right]
        if twoSum == target:
            return [left + 1, right + 1]
        elif twoSum > target:
            right -= 1
        else:
            left += 1
    return [-1, -1]

def main():
    numbers = [2, 7, 11, 15]
    target = 9
    expected = [1, 2]
    result = two_sum(numbers, target)
    assert result == expected
    print(result)

if __name__ == '__main__':
    main()
