from typing import List


def buy_and_sell_once(prices: List[int]) -> int:
    max_profit = 0
    min_price_so_far = float('-inf')
    for price_idx in range(len(prices)):
        max_profit_sale_today = prices[price_idx] - min_price_so_far
        max_profit = max(max_profit, max_profit_sale_today)
        min_price_so_far = min(min_price_so_far, prices[price_idx])
    if min_price_so_far == float('-inf'):
        return 0
    return max_profit


def buy_and_sell_stock_twice(prices: List[int]) -> int:
    # Forward pass: For each day record the max profit if we sell on that
    # day
    first_buy_and_sell_profits = [0 for _ in range(len(prices))]
    min_price_so_far, max_profit = float('inf'), 0
    for idx, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        # get max profit for that day: price - min_price = profit
        max_profit = max(max_profit, price - min_price_so_far)
        # record max profit for prices[idx]
        first_buy_and_sell_profits[idx] = max_profit

    # Backward phase: find the max profit if we make the second buy
    # on that day
    max_price_so_far = float('-inf')
    idx = len(prices) - 1
    while idx >= 1:
        max_price_so_far = max(max_price_so_far, prices[idx])
        max_profit = max(max_profit, max_price_so_far - prices[idx] + first_buy_and_sell_profits[idx])
        idx -= 1
    return max_profit


def test_buy_and_sell_once():
    stock_prices = [310,310,275,275,260,260,260,230,230,230]
    expected = 30
    max_profit = buy_and_sell_once(prices=stock_prices)
    assert max_profit == expected, f'Got {max_profit}, expected {expected}'


def test_buy_and_sell_twice():
    prices = [3,3,5,0,0,3,1,4]
    expected = 6
    result = buy_and_sell_stock_twice(prices=prices)
    assert result == expected, f'Got {result} expected {expected}'


if __name__ == "__main__":
    test_buy_and_sell_twice()
