#!/usr/bin/python

import argparse
from typing import List


def find_max_profit(prices: List[int]):
    largest_difference = prices[1] - prices[0]

    for index in range(1, len(prices)):
        def get_difference(compare: int): return compare - prices[index]
        differences = map(get_difference, prices[index + 1:])
        largest_difference = max([*differences, largest_difference])

    return largest_difference


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
