from typing import List

def sort_scores(scores: List[int], max_score: int) -> List[int]:
    result = []
    counts = [0 for _ in range(max_score + 1)]
    for num in scores:
        counts[num] += 1
    # walk backwards and add scores in descending order
    # forward for ascending
    count_idx = len(counts) - 1
    while count_idx >= 0:
        count = counts[count_idx]
        for _ in range(count):
            # Count is like a key value store: the keys are the indices
            # and the values are the counts in the score list
            result.append(count_idx)
        count_idx -= 1
    return result

def test():
    scores = [37, 89, 41, 65, 91, 53]
    max_score = 100
    print(scores)
    result = sort_scores(scores, max_score)
    print(result)

if __name__ == "__main__":
    test()

