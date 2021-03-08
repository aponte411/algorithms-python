from typing import List

def permutations(A: List[int]) -> List[List[int]]:
    """
    O(n * n!) time, O(n *n!) space
    """
    def dfs(index):
        if index == len(A) - 1:
            # make a shallow copy
            result.append(A.copy())
            return
        for next_index in range(index, len(A)):
            # swap index with next_index
            A[index], A[next_index] = A[next_index], A[index]
            # recurse
            dfs(index + 1)
            # swap again
            A[index], A[next_index] = A[next_index], A[index]
    result: List[List[int]] = []
    dfs(index=0)
    return result

def test():
    nums = [1,2,3]
    expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]
    result = permutations(A=nums)
    assert result == expected, f'Expected {expected}, got {result}'
    print(result)

if __name__ == "__main__":
    test()
