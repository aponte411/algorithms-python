MAX_INT = 2**31

def my_atoi(string: str) -> int:
    if string == "":
        return 0
    new_string = string.strip()
    sign = 1
    if new_string and new_string[0] == '-':
        sign = -1
        new_string = new_string[1:]
    elif new_string and new_string[0] == '+':
        new_string = new_string[1:]

    number = 0
    for char in string:
        if char.isdigit():
            number = (number*10)+int(char)
        else:
            break
    result = (number*sign)
    if result >= MAX_INT:
        return MAX_INT - 1
    elif result < - MAX_INT:
        return - MAX_INT
    return result

def test():
    string = "   -42"
    expected = -42
    result = my_atoi(string)
    print(result)

if __name__ == "__main__":
    test()
