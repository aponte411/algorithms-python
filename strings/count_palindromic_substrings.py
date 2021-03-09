import pytest


"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even when they consist of same characters.

Palindrome: the word is the same forwards and backwards

a
b
b
racecar

#Example 1
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

#Example 2
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

#Constraint
The input string length won't exceed 1000.

Solution

Multiple palindromes have the same centers. If we choose a center, we can continue to expand around it as long as we can make larger and larger palindromes.

Let's take the string "lever" as an example: if you choose the character 'v' as the center, one can see that the palindromes "v" and "eve" are possible. However, the final expansion "lever" is not a palindrome (the first and last characters don't match).

Algorithm

We choose all possible centers for potential palindromes:

Every single character in the string is a center for possible odd-length palindromes
Every pair of consecutive characters in the string is a center for possible even-length palindromes.
For every center, we can expand around it as long as we get palindromes (i.e. the first and last characters should match).
"""

def is_palindrome(substring: str, start: int, end: int) -> int:
    counts = 0
    # Work out way from the middle to the outside stopping once
    # we dont find a palindrome.
    while start >= 0 and end < len(substring) and substring[start] == substring[end]:
        start -= 1
        end += 1
        counts += 1
    return counts


def count_palindromes(string: str) -> int:
    # Palindromes are like onions, you remove the boundary characters and
    # you're left with another, smaller palindrome.
    # O(N^2) time, O(1) space
    counts = 0
    for center in range(len(string)):
        # odds
        counts += is_palindrome(string, center, center)
        # evens
        counts += is_palindrome(string, center, center+1)
    return counts



def test_count_palindromes():
    string = "abc"
    # ["a", "b", "c"]
    expected = 3
    result = count_palindromes(string)
    assert result == expected


pytest.main()
