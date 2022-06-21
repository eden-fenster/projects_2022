#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-02-06
Purpose: Random Snack Generator
"""
from typing import List
from dataclasses import dataclass


@dataclass
class State:
    """List of snacks we have in the house"""
    foods: List[str]
    quit: bool


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    state = State(foods=[],
                  quit=False)

    while True:
        print("\033[H\033[J")

        if state.quit:
            print('No more foods to add')
            print(''.join(state.foods))
            break

        state = get_food(state=state)


def get_food(state: State) -> State:
    """Get the food from the user"""

    foods = state.foods
    food_to_add = input('Add food to the list of snacks [q to quit]: ')

    if food_to_add == 'q':
        setattr(state, 'quit', True)
        return state

    foods.append(food_to_add)
    foods.append(' ')
    return State(foods=foods,
                 quit=False)


# --------------------------------------------------
if __name__ == '__main__':
    main()
