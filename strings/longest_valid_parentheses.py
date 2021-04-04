import pytest

def longest_valid_parentheses(s: str) -> int:
    # record indices in LIFO order
    stack = [-1] # use -1 as null value
    longest = 0
    for idx, char in enumerate(s):
        if char == '(':
            stack.append(idx)
        else:
            # pop the last parenthesis
            stack.pop()
            # if the stack is empty, add the idx
            if not stack:
                stack.append(idx)
            # else we calculate the length of the substring
            longest = max(longest, idx - stack[-1])
    return longest

def test():
    s = ")()())"
    expected = 4
    result = longest_valid_parentheses(s)
    assert result == expected

pytest.main()

