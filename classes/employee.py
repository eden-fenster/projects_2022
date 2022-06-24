#!/usr/bin/env python3
from dataclasses import dataclass


class Employee:

    def __init__(self, name, age, salary, pension):
        self._name = name
        self._age = age
        self._salary = salary
        self._pension = pension

    def give_raise(self, x: int):
        self._salary += x


bob = Employee('Bob Brown', 22, 10000, 1000)
bob.give_raise(x=2000)
print(vars(bob))


@dataclass
class Manager(Employee):

    def __init__(self, name, age, salary, pension, group):
        super().__init__(name, age, salary, pension)
        self._group = group


bobs_boss = Manager('Rachel Berry', 60, 50000, 70000, 'Back-End')
print(vars(bobs_boss))
