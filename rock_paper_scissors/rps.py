#!/usr/bin/python

import sys
from typing import Any, List


# For each player
# there are three options
# for every option of all other players

def multiply_list(list1: List[Any], list2: List[Any]):
    if not list1:
        return list2

    if not list2:
        return list1

    combined = []
    for item1 in list1:
        for item2 in list2:
            combined.append([*item1, *item2])

    return combined


def rock_paper_scissors(player_count):
    if player_count <= 0:
        return [[]]

    options = [["rock"], ["paper"], ["scissors"]]
    previous_combinations = rock_paper_scissors(player_count - 1)
    combinations = multiply_list(options, previous_combinations)

    return combinations


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
