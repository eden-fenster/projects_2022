from abc import abstractmethod
from typing import List


class Base():
    def __init__(self, name):
        print("In base class init")
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def talk(self):
        pass


class Dog(Base):
    def talk(self):
        print(f"Bark {self.name}")


class Cat(Base):
    def talk(self):
        print(f"Meow {self.name}")



animals: List[Base] = [Dog("Anoogie"), Cat("Tabbie"), Cat("It")]

for animal in animals:
    animal.talk()

