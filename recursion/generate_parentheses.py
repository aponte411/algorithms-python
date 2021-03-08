from typing import List

def generate_parenthesis(num_of_pairs: int) -> List[str]:
    def recursive_helper(curr_string: str, left: int, right: int):
        if len(curr_string) == 2 * num_of_pairs:
            result.append(curr_string)
            return
        # if we have more left parens then right add left
        if left < num_of_pairs:
            recursive_helper(curr_string+"(", left+1, right)
        # if we have less right than left parens, complete then by
        # adding a right paren
        if right < left:
            recursive_helper(curr_string+")", left, right+1)
    result: List[str] = []
    recursive_helper("", 0, 0)
    return result

def test():
    num_of_pairs = 3
    expected = ["((()))","(()())","(())()","()(())","()()()"]
    result = generate_parenthesis(num_of_pairs)
    print(result)
    assert result == expected

if __name__ == "__main__":
    test()


