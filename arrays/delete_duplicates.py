from typing import List

def delete_duplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    write_idx = 1
    for idx in range(1, len(nums)):
        if nums[write_idx - 1] != nums[idx]:
            nums[write_idx] = nums[idx]
            write_idx += 1
    return write_idx


def test_delete_duplicates():
    A = [2,3,5,5,7,11,11,11,13]
    result = delete_duplicates(nums=A)
    expected = 6
    assert result == expected, f'Expected {expected}, got {result}'
    print(f'Given {A}, after deleting duplicates the number of valid entries is {result}')

if __name__ == "__main__":
    test_delete_duplicates()
