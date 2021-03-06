"""
Is first come first served? FIFO
"""
from typing import List


def is_first_come_first_served(
    take_out_orders: List[int],
    dine_in_orders: List[int],
    served_orders: List[int],
):
    take_out, dine_in = 0, 0
    for order in served_orders:
        if take_out <= len(take_out_orders) - 1 and order == take_out_orders[take_out]:
            take_out += 1
        elif dine_in <= len(dine_in_orders) -1 and order == dine_in_orders[dine_in]:
            dine_in += 1
        else:
            return False

    if take_out != len(take_out_orders) or dine_in != len(dine_in_orders):
        return False
    return True

def test():
    take_out_orders = [1, 4, 5]
    dine_in_orders = [2, 3, 6]
    served_orders = [1, 2, 3, 4, 5, 6,]
    result = is_first_come_first_served(
        take_out_orders,
        dine_in_orders,
        served_orders,
    )
    expected = True
    assert result == expected


if __name__ == "__main__":
    test()
