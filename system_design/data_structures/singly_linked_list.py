from dataclasses import dataclass

@dataclass
class Node:
    val: int
    next: None

class LinkedList:
    def __init__(self):
        sentinel = Node(0)
        self.head = sentinel
        self.size = 0

    def get(self, index: int) -> Node:
        if index == 0:
            return self.head
        node = self.head
        for _ in range(index+1):
            node = node.head
        return node

    def add_at_head(self, val: int) -> None:
        self.add_at_index(0, val)

    def add_at_index(self, index: int, val: int) -> None:
        if index > self.size:
            return
        predecessor = self.head
        self.size += 1
        for _ in range(index):
            predecessor = predecessor.next

        new_node = Node(val)
        new_node.next = predecessor.next
        predecessor.next = new_node

    def delete_at_index(self, index: int):
        pass

def test():
    index= 0
    linked_list = LinkedList()
    result = linked_list.get(index)
    print(result)

if __name__ == "__main__":
    test()
