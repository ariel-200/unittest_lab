def main():

    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?

    

def discount(item_prices):
    """ Complete this function that returns the discount earned for a list of item prices
    If a customer has ordered three or more items, the cheapest item is free.
    Example: if this function is called with a list of [10, 4, 20] then return 4.
    Example: if the function is called with a list of [10, 10, 10, 10] then return 10
    Example: if the function is called with a list of [100, 3] then return 0
    """

    if len(item_prices) >= 3:
        return min(item_prices)
    else:
        return 0


if __name__ == '__main__':
    main()
