
def contains_perm(s1: str, s2: str) -> bool:
    # Count distribution of characters in constant space
    s1freq = [0]*26
    s2freq = [0]*26
    for i in range(len(s1)):
        s1freq[ ord(s1[i]) - 97 ] += 1
        s2freq[ ord(s2[i]) - 97 ] += 1
    # if the distributions match, theres a permumation
    if s1freq == s2freq:
        return True
    # if not, go through remainder of s2 and stop early
    # if distrubutions match
    for i in range(len(s1), len(s2)):
        s2freq[ ord(s2[i]) - 97 ] += 1
        s2freq[ ord(s2[i - len(s1)]) - 97 ] -= 1
        if s1freq == s2freq:
            return True
    return False

def main():
    s1 = "ab"
    s2 = "eidbaooo"
    result = contains_perm(s1, s2)
    expected = True
    assert result == expected
    print(result)

if __name__ == "__main__":
    main()
