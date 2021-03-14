import pytest
from typing import List

def merge_meetings(meetings: List[List[int]]) -> List[List[int]]:
    # Sort so we get the next meeting
    meetings = sorted(meetings)
    # Put the next meeting at the top
    merged = [meetings[0]]
    for curr_start, curr_end in meetings[1:]:
        last_start, last_end = merged[-1]
        if curr_start <= last_end:
            # merge
            merged[-1] = [last_start,max(last_end, curr_end)]
        else:
            merged.append([curr_start, curr_end])
    return merged

def test():
    meetings = [[1,3],[2,6],[8,10],[15,18]]
    expected = [[1,6],[8,10],[15,18]]
    result = merge_meetings(meetings)
    assert result == expected

pytest.main()

