def parity(n: int) -> int:
    # the parity of a word is 1 if the number of ones is
    # odd; the parity of a word is 0 if the number of ones is even.
    result = 0
    while n:
        # XOR
        result ^= n & 1
        n >>= 1
    return result
