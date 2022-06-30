#!/usr/bin/env python3
from abc import abstractmethod
from typing import List


class Robot:
    def __init__(self, name, metal, age, workplace):
        self._name = name
        self._metal = metal
        self._age = age
        self._workplace = workplace

    @property
    def name(self):
        return self._name

    @abstractmethod
    def make_food(self):
        pass


class PizzaRobot(Robot):
    def __init__(self, name, metal, age, workplace):
        super().__init__(name, metal, age, workplace)

    def make_food(self):
        print(f"{self._name} is making Pizza")


class GarlicBreadRobot(Robot):
    def __init__(self, name, metal, age, workplace):
        super().__init__(name, metal, age, workplace)

    def make_food(self):
        print(f"{self._name} is making Garlic Bread")


garlic_bread = GarlicBreadRobot('Leaf', 'Steel', 33, 'Dominos')
pizza = PizzaRobot('Pepperoni', 'foil', 22, 'Dominos')
robot_list: List[Robot] = [garlic_bread, pizza]

for robot in robot_list:
    robot.make_food()
