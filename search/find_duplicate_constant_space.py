from typing import List

def find_repeating(numbers: List[int]):
    floor, ceiling = 1, len(numbers) - 1
    while floor < ceiling:
        pivot = floor + ((ceiling - floor)//2)
        # split into two buckets: lower and upper
        lower_floor, lower_ceiling = floor, pivot
        upper_floor, upper_ceiling = pivot + 1, ceiling
        # count numbers in lower
        in_lower = 0
        for num in numbers:
            if lower_floor <= num <= lower_ceiling:
                in_lower += 1
        uniq_in_lower = lower_ceiling - lower_floor + 1
        if in_lower > uniq_in_lower:
            # duplicate is in lower
            floor, ceiling = lower_floor, lower_ceiling
        else:
            # duplicate is in upper bucket
            floor, ceiling = upper_floor, upper_ceiling
    return floor


def test():
    numbers = [1,2,3,2]
    expected = 2
    result = find_repeating(numbers)
    assert result == expected
    print(result)


if __name__ == "__main__":
    test()
