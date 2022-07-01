#!/usr/bin/env python3
import math
from abc import abstractmethod


class Shape:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def shape_circumfurence(self):
        pass

    @abstractmethod
    def shape_area(self):
        pass


class Square(Shape):
    def __init__(self, name, length):
        super().__init__(name)
        self._length = length

    def shape_circumfurence(self) -> int:
        return self._length * 4

    def shape_area(self) -> int:
        return math.pow(self._length, 2)


