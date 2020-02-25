#!/usr/bin/python

import sys
from typing import List

cache = {}


def making_change(amount: int, denominations: List[int]):
    if (amount == 0 or len(denominations) <= 1):
        return 1

    if f'{amount}-{denominations}' in cache:
        return cache[f'{amount}-{denominations}']

    # There is always only one way with only pennies (with just pennies)
    total = 1

    # We will just count the ways that aren't pennies
    denomination = denominations[1]
    for variation in range(0, amount // denomination):
        amount_left = amount - variation * denomination
        # We subtract one since we don't want to count the pennies solution more then once
        total += making_change(amount_left, denominations[1:]) - 1
        total += 1

    cache[f'{amount}-{denominations}'] = total
    return total


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
