#!/usr/bin/env python3
from dataclasses import dataclass


class Robot:
    metal: str = 'Iron'
    age: int = 24

    def __init__(self, metal, age):
        self._metal = metal
        self._age = age
        pass

    def print_robot(self):
        print(self._metal, end=', ')
        print(self._age)


robot = Robot('Steel', 99)
robot.print_robot()


@dataclass
class PizzaRobot(Robot):
    ptype: str = "Hawaiian"
    workplace: str = 'Dominos'

    def __init__(self, metal, age, ptype, workplace):
        super().__init__(metal, age)
        self._ptype = ptype
        self._workplace = workplace


pizza_robot = PizzaRobot('Mercury', 17, 'Olives', 'Pizza Hut')
print(vars(pizza_robot))
