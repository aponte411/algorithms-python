import pytest
from typing import List


def is_valid_ip(s: str) -> bool:
    return 0 <= int(s) <= 255


def backtrack(s: str, index: str, address: str, results: List[str]):
    """DFS backtracking approach, adding the address when we reach a leaf"""
    # if we reach the end of the string, or our current partial answer equals 4,
    # add it
    if index == len(s) and len(address) == 4:
        results.append(".".join(address))
        return
    # if its not a valid ip, and were at the end, return
    if index == len(s):
        return
    # move forward and build ip address, once we find a valid address
    # search through the possible ips that can be made from partial_ip
    for next_idx in range(index, len(s)):
        partial_ip = s[index:next_idx+1]
        if is_valid_ip(partial_ip):
            # backtrack
            backtrack(
                s,
                next_idx+1,
                address + [partial_ip],
                results,
            )
        # if we find a leading zero, break out of the for loop
        if s[next_idx] == "0":
            break


def get_valid_ip_addresses(s: str) -> List[str]:
    results: List[str] = []
    backtrack(s, 0, [], results)
    return results


@pytest.mark.parametrize(
    "input, expected",
    [
        ("25525511135", ["255.255.11.135","255.255.111.35"]),
        ("0000", ["0.0.0.0"]),
    ]
)
def test_get_valid_ip_addresses(input, expected):
    result = get_valid_ip_addresses(s=input)
    assert result == expected


pytest.main()
