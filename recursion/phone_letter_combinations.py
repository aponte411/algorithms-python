from typing import List, Tuple

DIGIT_MAPPING: Tuple[str] = ('0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')

def letter_combinations(digits: str) -> List[str]:
    def dfs(digit_index, partial_combination):
        if digit_index == len(digits):
            result.append(''.join(partial_combination))
            return
        # Get digit mapping
        digit = DIGIT_MAPPING[int(digits[digit_index])]
        for char in digit:
            # Overwrite partial combination
            partial_combination[digit_index] = char
            # recurse
            dfs(digit_index + 1)
        # end search
    result: List[str] = []
    # Use list of '0' strings
    partial_solution = ['0' for _ in range(len(digits))]
    dfs(0, partial_solution)
    return result
