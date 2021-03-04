from typing import List

def palindrome_decomposition(text: str) -> List[List[str]]:
    """
    O(n * 2^n) time, O(n * 2^n) space
    """
    def helper(index, partial_partition):
        if index == len(text):
            # Create shallow copy: construct a new list and populate
            # it with references to the child objects found in the original.
            result.append(partial_partition.copy())
            return
        # Go one ahead
        for i in range(index+1, len(text)+1):
            # get current prefix up until i and check if palindrome by
            # reversing
            prefix = text[index:i]
            if prefix == prefix[::-1]:
                # create shallow copy of prefix by setting it as list
                helper(
                    index=i,
                    partial_partition=[prefix],
                )
        # end search
    result: List[List[str]] = []
    helper(index=0, partial_partition=[])
    return result
