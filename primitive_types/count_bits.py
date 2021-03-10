def count_bits(n: int) -> int:
    num_bits = 0
    mask = 1
    for _ in range(32):
        if n & mask != 0:
            num_bits += 1
        mask <<= 1
    return num_bits

def test():
    n = 12
    expected = 2
    result = count_bits(n)
    print(result)

if __name__ == "__main__":
    test()
