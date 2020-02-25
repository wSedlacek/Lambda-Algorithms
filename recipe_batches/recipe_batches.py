#!/usr/bin/python

import math
from typing import Dict


def recipe_batches(recipe: Dict[str, int], ingredients: Dict[str, int]):
    batches_made = 0
    while True:
        for ingredient, number_required in recipe.items():

            if ingredient not in ingredients or ingredients[ingredient] < number_required:
                return batches_made

            ingredients[ingredient] -= number_required

        batches_made += 1


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
