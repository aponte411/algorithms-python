from typing import List


def wiggle_max_length_recursive(nums: List[int]) -> int:
    def calculate_max_count(index: int, is_up: bool) -> int:
        max_count = 0
        for next_idx in range(index+1, len(nums)):
            if (is_up and nums[next_idx] > nums[index]) or (not is_up and nums[next_idx] < nums[index]):
                # recursively calculate count
                count = calculate_max_count(next_idx, not is_up)
                max_count = max(max_count, count + 1)
        return max_count

    # ups
    is_up_max = calculate_max_count(0, True)
    not_up_max = calculate_max_count(0, False)
    # Max of both + 1 is global max
    wiggle_max = max(is_up_max, not_up_max) + 1
    return wiggle_max

def test():
    nums = [1,17,5,10,13,15,10,5,16,8]
    expected = 6
    result = wiggle_max_length_recursive(nums)
    print(result)

if __name__ == "__main__":
    test()
