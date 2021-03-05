from typing import List


def reverse(message: List[int], start: int, end: int):
    while start < end:
        message[start], message[end] = message[end], message[start]
        start += 1
        end -= 1


def reverse_words(message: List[str]):
    # first reverse all characters
    reverse(message, 0, len(message) - 1)
    curr_start_of_word = 0
    for msg_idx in range(len(message) + 1):
        if msg_idx == len(message) or message[msg_idx] == " ":
            reverse(message, curr_start_of_word, msg_idx - 1)
            curr_start_of_word = msg_idx + 1
    print(message)

def test():
    message = list('cake thief')
    expected = list('thief cake')
    reverse_words(message)


if __name__ == "__main__":
    test()
