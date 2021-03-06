from typing import List
import random

def get_random(floor: int, ceiling: int) -> int:
    return random.randrange(floor, ceiling + 1)

def knuth_shuffle(nums: List[int]) -> None:
    for idx in range(len(nums)-1):
        # Choose random, not yet placed idx
        random_idx = get_random(idx, len(nums)-1)
        if idx != random_idx:
            nums[idx], nums[random_idx] = nums[random_idx], nums[idx]

def test():
    nums = [1, 2, 3, 4, 5]
    print(f'Before {nums}')
    knuth_shuffle(nums)
    print(f'After {nums}')

if __name__ == "__main__":
    test()
