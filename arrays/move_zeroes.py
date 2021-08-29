from typing import List


def move_zeroes(nums: List[int]) -> List[int]:
    """
    Given an integer array nums, move all 0's to the
    end of it while maintaining the relative order
    of the non-zero elements.

    Note that you must do this in-place without making
    a copy of the array.
    """
    result = []
    zeroes = 0
    for num in nums:
        if num == 0:
            zeroes += 1
        else:
            result.append(num)

    while zeroes != 0:
        result.append(0)
        zeroes -= 1

    nums[:] = result
    return nums




def main():
    nums = [0, 1, 0, 3, 12]
    expected = [1, 3, 12, 0, 0]
    result = move_zeroes(nums)
    assert result == expected
    print(result)

if __name__ == '__main__':
    main()
