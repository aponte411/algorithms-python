from typing import List

def get_products_except_at_index(nums: List[int]) -> List[int]:
    if len(nums) < 2:
        raise ValueError('You need at least 2 values')
    # Greedily go through the integers and get the products of all integers
    # before the current index. Then go backwards and multiply the product by
    # the previous products.
    products = [None for _ in range(len(nums))]
    # Start with 1
    product = 1
    # forward pass
    for i in range(len(nums)):
        products[i] = product
        product *= nums[i]
    # backward pass
    product = 1
    for i in range(len(nums)-1, -1, -1):
        # Multiply product_i (last product) by the current
        # product and walk backwards
        products[i] *= product
        product *= nums[i]
    return products
def test():
    inputs = [1, 2, 3]
    expected = [6, 3, 2]
    result = get_products_except_at_index(nums=inputs)
    print(result)
    assert result == expected

if __name__ == "__main__":
    test()
