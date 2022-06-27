#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-27-06
Purpose: Random Snack Generator
"""
from typing import List
import random
from dataclasses import dataclass


@dataclass
class Food:
    """A snack"""
    food: str
    is_in_house: bool

    def __init__(self, food: str, is_in_house: bool):
        self._food = food
        self._is_in_house = is_in_house

    def get_food(self) -> str:
        return self._food

    def is_it_in_house(self) -> bool:
        return self._is_in_house

    def add_to_house(self):
        self._is_in_house = True

    def we_need_more_of_it(self):
        self._is_in_house = False

    def print_food(self) -> str:
        return self._food + '\n' + 'Do we have it at home ? ' + str(self._is_in_house)


class FoodList(Food):
    food_list: List[Food]
    num_of_foods: int

    def __init__(self, food_list: List[Food]):
        self._food_list = food_list
        self._num_of_foods = 0

    def add_food(self, food_to_add: Food):
        self._food_list.append(food_to_add)
        self._num_of_foods += 1

    def choose_random_food(self) -> Food:
        return random.choice(self._food_list)

    def print_list(self):
        printed_list: str = ''
        for i in range(0, len(self._food_list)):
            printed_list += self._food_list[i].print_food()
        return printed_list


apple: Food = Food(food='apple', is_in_house=True)
banana: Food = Food(food='banana', is_in_house=False)
list_of_food: List[Food] = []
foods: FoodList = FoodList(food_list=list_of_food)
foods.add_food(food_to_add=apple)
foods.add_food(food_to_add=banana)
random_food: Food = foods.choose_random_food()
print(random_food.print_food())
