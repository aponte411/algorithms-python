import unittest
from typing import List, Tuple

def max_duffel_bag_of_cakes(cake_tuples: List[Tuple[int, int]], weight_capacity: int) -> int:
    # Build table with weight capacity as key and maxValue of duffel bag at index i
    maxValues = [0]*(weight_capacity+1)
    # For every weight capacity
    for capacity in range(weight_capacity+1):
        # For every cake, value pair in cake tuples
        for cake_weight, cake_value in cake_tuples:
            # If we have an invalid cake with non-zero value
            if cake_weight == 0 and cake_value != 0:
                return float('inf')
            # Can we use this cake?
            if cake_weight <= capacity:
                # get max value using this cake (use weight and add value)
                with_cake = maxValues[capacity - cake_weight] + cake_value
                # If this new max value with cake adds something new, update
                maxValues[capacity] = max(maxValues[capacity], with_cake)
    return maxValues[weight_capacity]


class Test(unittest.TestCase):

    def test_one_cake(self):
        actual = max_duffel_bag_of_cakes([(2, 1)], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_two_cakes(self):
        actual = max_duffel_bag_of_cakes([(4, 4), (5, 5)], 9)
        expected = 9
        self.assertEqual(actual, expected)

    def test_only_take_less_valuable_cake(self):
        actual = max_duffel_bag_of_cakes([(4, 4), (5, 5)], 12)
        expected = 12
        self.assertEqual(actual, expected)

    def test_lots_of_cakes(self):
        actual = max_duffel_bag_of_cakes([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7)
        expected = 12
        self.assertEqual(actual, expected)

    def test_value_to_weight_ratio_is_not_optimal(self):
        actual = max_duffel_bag_of_cakes([(51, 52), (50, 50)], 100)
        expected = 100
        self.assertEqual(actual, expected)

    def test_zero_capacity(self):
        actual = max_duffel_bag_of_cakes([(1, 2)], 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_cake_with_zero_value_and_weight(self):
        actual = max_duffel_bag_of_cakes([(0, 0), (2, 1)], 7)
        expected = 3
        self.assertEqual(actual, expected)

    def test_cake_with_non_zero_value_and_zero_weight(self):
        actual = max_duffel_bag_of_cakes([(0, 5)], 5)
        expected = float('inf')
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
