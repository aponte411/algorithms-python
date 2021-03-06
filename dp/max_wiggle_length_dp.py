from typing import List

def max_wiggle_length_dp(nums: List[int]) -> int:
    if len(nums) < 2:
        return len(nums)

    up_memo = [0 for _ in range(len(nums))]
    down_memo = [0 for _ in range(len(nums))]
    # outer loop is the length i
    for i in range(1, len(nums)):
        # inner loop is the max count
        for j in range(0, i):
            if nums[i] > nums[j]:
                up_memo[i] = max(up_memo[i], down_memo[j] + 1)
            elif nums[i] < nums[j]:
                down_memo[i] = max(down_memo[i], up_memo[j] + 1)
    # return max of length - 1
    return 1 + max(up_memo[len(nums)-1], down_memo[len(nums)-1])

def test():
    nums = [1,7,4,9,2,5]
    expected = 6
    result = max_wiggle_length_dp(nums)
    print(result)

if __name__ == "__main__":
    test()
