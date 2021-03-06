from typing import List

def find_rotation_point(words: List[str]) -> int:
    # Store first word
    first_word = words[0]
    floor, ceiling = 0, len(words)-1
    while floor < ceiling:
        # Guess a point between floor and ceiling
        guess = floor + ((ceiling - floor)//2)
        # If our guess if after the first word,
        # the rotation point is somewhere to the right
        # because every item after our rotation point is
        # alphabetically before the first word
        if words[guess] > first_word:
            floor = guess
        else:
            ceiling = guess
        # Once they converge, the floor is the last item added
        # before starting
        if floor + 1 == ceiling:
            return ceiling
    # If we dont find a rotation point
    # return -1
    return -1

def test():
    words = [
        'ptolemaic',
        'retrograde',
        'supplant',
        'undulate',
        'xenoepist',
        'asymptote',
        'babka',
        'banoffee',
        'engender',
        'karpatka',
        'othellolagkage',
    ]
    expected = 5
    result = find_rotation_point(words)
    assert expected == result


if __name__ == "__main__":
    test()

