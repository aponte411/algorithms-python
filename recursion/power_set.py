from typing import List

def generate_power_set_recursively(input_set: List[int]) -> List[List[int]]:
    """
    O(2^n) recursive calls O(n) time per call, O(n2^n) time and space,
    only printing the subsets brings the space down to O(n) space.
    """
    def power_set(to_be_selected, selected_so_far) -> None:
        if to_be_selected == len(input_set):
            power_sets.append(selected_so_far)
            return
        # Without
        power_set(to_be_selected + 1, selected_so_far)
        # With
        power_set(to_be_selected + 1, selected_so_far + [input_set[to_be_selected]])

    power_sets: List[List[int]] = []
    power_set(0, [])
    return power_sets

def generate_power_set_bit_array(input_set: List[int]) -> List[List[int]]:
    """
    O(n2^n) time, O(n) space
    """
    power_set = []
    for int_for_subset in range(1 << len(input_set)):
        bit_array = int_for_subset
        subset = []
        while bit_array:
            subset.append(input_set[int(math.log2(bit_aray & ~(bit_array - 1)))])
            bit_array &= bit_array - 1
        power_set.append(subset)
    return power_set



