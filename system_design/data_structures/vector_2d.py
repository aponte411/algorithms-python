from typing import List

class Vector2D:
    def __init__(self, vector: List[List[int]]):
        self.nums = []
        for inner_list in vector:
            for num in inner_list:
                self.nums.append(num)
        self.position = 0

    def next(self) -> int:
        val = self.nums[self.position]
        self.position += 1
        return val

    def has_next(self) -> int:
        return self.position < len(self.nums)


def test():
    vector = [[1, 2, 3], [4, 5, 0]]
    vector2d = Vector2D(vector=vector)
    while vector2d.nums:
        try:
            print(vector2d.next())
        except IndexError:
            break

if __name__ == "__main__":
    test()
