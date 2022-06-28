from abc import abstractmethod


class Robot:
    def __init__(self, name, metal, age, workplace):
        self._name = name
        self._metal = metal
        self._age = age
        self._workplace = workplace

    @property
    def name(self):
        return self._name

    @property
    def workplace(self):
        return self._workplace

    @abstractmethod
    def make_food(self):
        pass


class PizzaRobot(Robot):
    def make_food(self):
        print(f"Making Pizza")


class GarlicBreadRobot(Robot):
    def make_food(self):
        print(f"Making Garlic Bread")
