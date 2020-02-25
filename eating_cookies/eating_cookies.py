#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# input -> output
# 0 -> 1
# 1 -> 1
# 2 -> 2
# 3 -> 4
# 4 -> 7
# 5 -> 13
# 10 -> 274
# This is Tribonacci but starting at index of 1
# 0 1 1 2 4 7 13 24 44 81 149 274
# T(n) = T(n-1) + T(n-2) + T(n-3)


def eating_cookies(n: int, cache=None):
    sequence = [0, 1, 1]

    for i in range(3, n + 2):
        sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i - 3])

    return sequence[-1]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
