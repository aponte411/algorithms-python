from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    def top_down(curr_total: int, cand_index: int, partial_combo: List[int]):
        if curr_total == 0:
            result.append(partial_combo.copy())
            return
        if curr_total < 0:
            return
        if cand_index == len(candidates):
            return
        cand = candidates[cand_index]
        while curr_total >= 0:
            top_down(curr_total, cand_index+1, partial_combo)
            partial_combo = partial_combo + [cand]
            curr_total -= cand
        # end search
    result: List[List[int]] = []
    top_down(target, 0, [])
    return result


def test():
    candidates = [2,3,6,7]
    expected = [[7], [2, 2, 3]]
    target = 7
    results = combination_sum(candidates, target)
    assert results == expected
    print(results)


if __name__ == "__main__":
    test()
