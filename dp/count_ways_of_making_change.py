from typing import List
import unittest


def coin_change(amount: int, coins: List[int]) -> int:
    """
    We use a bottom-up algorithm to build up a table ways_of_doing_n_cents
    such that ways_of_doing_n_cents[k] is how many ways we can get to k cents
    using our coin denominations. We start with the base case that there's one
    way to create the amount zero, and progressively add each of our denominations.
    The number of new ways we can make a higher_amount when we account for a new
    coin is simply ways_of_doing_n_cents[higher_amount - coin], where we know that
    value already includes combinations involving coin (because we went bottom-up,
    we know smaller values have already been calculated).
    """
    # table of ways
    ways = [0]*(amount+1)
    ways[0] = 1
    for coin in coins:
        for target in range(1, amount+1):
            if coin <= target:
                ways[target] = ways[target] + ways[target - coin]

    return ways[amount]


class Test(unittest.TestCase):
    def test_sample_input(self):
        actual = coin_change(4, (1, 2, 3))
        expected = 4
        self.assertEqual(actual, expected)

    def test_one_way_to_make_zero_cents(self):
        actual = coin_change(0, (1, 2))
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        actual = coin_change(1, ())
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        actual = coin_change(5, (25, 50))
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        actual = coin_change(50, (5, 10))
        expected = 6
        self.assertEqual(actual, expected)

    def test_change_for_one_dollar(self):
        actual = coin_change(100, (1, 5, 10, 25, 50))
        expected = 292
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
